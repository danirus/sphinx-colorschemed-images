export class SphinxColorschemeImageHandler {
  constructor(options={}) {
    this._schemes = [];
    this._mediaqs = [];

    // If options are not given or if it is given with a key 'auto'
    // and a boolean value true, then the instance created will add
    // an event listener for changes on prefers-color-scheme to
    // update images accordingly.
    this._auto = options.hasOwnProperty('auto')
      ? options['auto'] === true
      : true;

    const meta_prop = document.querySelector('meta[name="color-scheme"]');
    let meta_schemes = (meta_prop != null) ? meta_prop.content : "";

    if (meta_schemes.length > 0) {
      const schemes = meta_schemes.split(" ");
      for (const item of schemes) {
        this._schemes.push(item.trim());
      }
    } else {
      this._schemes = ['light', 'dark'];
    }

    for (const scheme of this._schemes) {
      const q = globalThis.matchMedia(`(prefers-color-scheme: ${scheme})`);
      if (q.matches) {
        this.activate(scheme);
      }
      if (this._auto === true) {
        q.addEventListener('change', e => {
          if (e.matches) {
            console.log('event:', e);
            this.activate(scheme);
          }
        });
        this._mediaqs.push(q);
      }
    }
  }

  activate = (scheme) => {
    const data_att = `data-alt-src-color-scheme-${scheme}`;
    const images = document.querySelectorAll(`img[${data_att}]`);
    for (const img of images) {
      const new_img = new Image();
      const new_src = img.getAttribute(data_att);
      new_img.src = new_src;
      new_img.addEventListener('load', () => {
        img.src = new_img.src;
      });
      new_img.addEventListener('error', () => {
        console.error(`Could not replace image ${img.src} with ${new_src}.`);
      });
      if (new_img.complete) {
        img.src = new_img.src;
      }
    }
  }
}
