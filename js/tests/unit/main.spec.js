import { SphinxColorschemeImageHandler } from '../../src/main';
import { getFixture, clearFixture } from '../helpers/fixture.js';


const template_1 = [
  '<div>',
  '  <img ',
  '    alt="A balloon icon" class="align-right"',
  '    data-alt-src-color-scheme-dark="balloon.dark.png"',
  '    data-alt-src-color-scheme-light="balloon.light.png"',
  '    src="balloon.light.png"',
  '    width="200"',
  '  >',
  '</div>',
];

describe('Image src attribute changes', () => {
  let fixtureEl;

  beforeAll(() => {
    fixtureEl = getFixture();

    // Be sure that prefers-color-scheme matches when is 'dark'.
    spyOn(globalThis, 'matchMedia').and.callFake(
      (media_query) => {
        const matches = media_query.includes('dark') ? true : false;
        return {
          matches,    // prefers-color-scheme: dark
          addEventListener: (evt_name, evt_obj) => {},
        };
      }
    );
  });

  afterEach(() => {
    clearFixture();
  });

  it('Check that the src changes from light to dark URL', () => {
    // Be sure that the Image loads.
    spyOn(globalThis, 'Image').and.callFake(
      () => {
        return {
          src: '',
          addEventListener: (evt_name, evt_cb) => {
            if (evt_name === 'load') evt_cb();
          }
        }
      }
    )

    fixtureEl.innerHTML = template_1.join('');

    // When loading the template the 'src' attribute of
    // the image corresponds to the light version of it.
    let img = document.querySelector('img');
    expect(img.getAttribute('src')).toEqual('balloon.light.png');

    new SphinxColorschemeImageHandler({auto: false});

    // After SphinxColorschemeImageHandler is used,
    // the image has switch to the dark theme version.
    img = document.querySelector('img');
    expect(img.getAttribute('src')).toEqual('balloon.dark.png');
  });

  it('Check that the src changes from light to dark URL, immediately', () => {
    // Be sure that the Image loads.
    spyOn(globalThis, 'Image').and.callFake(
      () => {
        return {
          complete: true,  // This will change the image immediately.
          src: '',
          addEventListener: (evt_name, evt_cb) => {}
        }
      }
    )

    fixtureEl.innerHTML = template_1.join('');

    // When loading the template the 'src' attribute of
    // the image corresponds to the light version of it.
    let img = document.querySelector('img');
    expect(img.getAttribute('src')).toEqual('balloon.light.png');

    new SphinxColorschemeImageHandler({auto: false});

    // After SphinxColorschemeImageHandler is used,
    // the image has switch to the dark theme version.
    img = document.querySelector('img');
    expect(img.getAttribute('src')).toEqual('balloon.dark.png');
  });

  it('Check that the src does not change if it does not load', () => {
    // Be sure that the Image loads.
    spyOn(globalThis, 'Image').and.callFake(
      () => {
        return {
          src: '',
          addEventListener: (evt_name, evt_cb) => {
            if (evt_name === 'error') evt_cb();
          }
        }
      }
    )

    fixtureEl.innerHTML = template_1.join('');

    // When loading the template the 'src' attribute of
    // the image corresponds to the light version of it.
    const expected_src = 'balloon.light.png';
    let img = document.querySelector('img');
    expect(img.getAttribute('src')).toEqual(expected_src);

    new SphinxColorschemeImageHandler({auto: false});

    // Given that the image did not load, the src is the same.
    img = document.querySelector('img');
    expect(img.getAttribute('src')).toEqual(expected_src);
  });
});


describe('Image src attribute changes when change event is triggered', () => {
  let fixtureEl;
  let changeSchemeCallback;

  beforeAll(() => {
    fixtureEl = getFixture();

    // Be sure that prefers-color-scheme matches when is 'dark'.
    spyOn(globalThis, 'matchMedia').and.callFake(
      (media_query) => {
        const matches = media_query.includes('dark') ? true : false;
        return {
          matches,    // prefers-color-scheme: dark
          addEventListener: (evt_name, evt_obj) => {
            console.log("setting up changeSchemeCallback");
            if (matches)
              changeSchemeCallback = evt_obj;
          },
        };
      }
    );

    spyOn(globalThis, 'Image').and.callFake(
      () => {
        return {
          src: '',
          addEventListener: (evt_name, evt_cb) => {
            if (evt_name === 'load') evt_cb();
          }
        }
      }
    )
  });

  afterEach(() => {
    clearFixture();
  });

  it('Image is loaded 100ms after calling the test case', async () => {
    fixtureEl.innerHTML = template_1.join('');

    // When loading the template the 'src' attribute of
    // the image corresponds to the light version of it.
    let img = document.querySelector('img');
    expect(img.getAttribute('src')).toEqual('balloon.light.png');

    new SphinxColorschemeImageHandler();  // auto is true by default.

    changeSchemeCallback({matches: true});
    img = document.querySelector('img');
    expect(img.getAttribute('src')).toEqual('balloon.dark.png');
  });
});

// --------------------------------------------------------------------
const template_2 = [
  '<html>',
  '  <head><meta name="color-scheme" content="dark light" /></head>',
  '  <body>',
  '    <div>',
  '      <img ',
  '        alt="A balloon icon" class="align-right"',
  '        data-alt-src-color-scheme-dark="balloon.dark.png"',
  '        data-alt-src-color-scheme-light="balloon.light.png"',
  '        src="balloon.light.png"',
  '        width="200"',
  '      >',
  '    </div>',
  '  </body>',
  '</html>',
];

describe('Color schemes loaded from meta tag', () => {
  let fixtureEl;
  const schemeRE = /\(prefers-color-scheme: (?<scheme>\w+)\)/;
  let schemesRead = [];

  beforeAll(() => {
    fixtureEl = getFixture();

    // Be sure that prefers-color-scheme matches when is 'dark'.
    spyOn(globalThis, 'matchMedia').and.callFake(
      (media_query) => {
        const match = media_query.match(schemeRE);
        if (match) {
          schemesRead.push(match.groups['scheme']);
        }

        return {
          matches: false,
          addEventListener: (evt_name, evt_obj) => {},
        };
      }
    );
  });

  afterEach(() => {
    clearFixture();
    schemesRead = [];
  });

  it('Reads the available color schemes from a meta tag', () => {
    fixtureEl.innerHTML = template_2.join('');

    expect(schemesRead).toEqual([]);
    new SphinxColorschemeImageHandler({auto: false});
    expect(schemesRead).toEqual(['dark', 'light']);
  });
});


// --------------------------------------------------------------------
describe('Initialize with options auto=true and auto=false', () => {
  beforeAll(() => {
    // Be sure that prefers-color-scheme matches when is 'dark'.
    spyOn(globalThis, 'matchMedia').and.callFake(
      (media_query) => {
        return {
          matches: false,
          addEventListener: (evt_name, evt_obj) => {},
        };
      }
    );
  });

  it('Check that eventListeners have been added to _mediaqs', () => {
    const hdl = new SphinxColorschemeImageHandler({auto: true});
    expect(hdl._mediaqs.length).toEqual(2);
  });

  it('Check that eventListends have not been added to _mediaqs', () => {
    const hdl = new SphinxColorschemeImageHandler({auto: false});
    expect(hdl._mediaqs.length).toEqual(0);
  });

  it('Check that it is auto is true by default', () => {
    const hdl = new SphinxColorschemeImageHandler();
    expect(hdl._mediaqs.length).toEqual(2);  // Only if auto is true.
  });
});
