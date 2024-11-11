import { SphinxColorschemeImageHandler } from "./main";

function runWhenDOMContentLoaded(cb) {
  if (document.readyState != 'loading') {
    cb();
  } else if (document.addEventListener) {
    document.addEventListener('DOMContentLoaded', cb);
  } else {
    document.attachEvent('onreadystatechange', function() {
      if (document.readyState == 'complete') cb();
    });
  }
}

function addSphinxColorschemedImageHandler() {
  return new SphinxColorschemeImageHandler();
}

runWhenDOMContentLoaded(addSphinxColorschemedImageHandler);
