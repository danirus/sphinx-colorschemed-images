/*!
  * sphinx-colorschemed-images v0.1.0 (https://github.com/danirus/sphinx-colorschemed-images).
  * Copyright 2024 Daniela Rus Morales.
  * Licensed under MIT (https://github.com/danirus/sphinx-colorschemed-images/blob/main/LICENSE).
  */
function _arrayLikeToArray(r, a) {
  (null == a || a > r.length) && (a = r.length);
  for (var e = 0, n = Array(a); e < a; e++) n[e] = r[e];
  return n;
}
function _createForOfIteratorHelperLoose(r, e) {
  var t = "undefined" != typeof Symbol && r[Symbol.iterator] || r["@@iterator"];
  if (t) return (t = t.call(r)).next.bind(t);
  if (Array.isArray(r) || (t = _unsupportedIterableToArray(r)) || e) {
    t && (r = t);
    var o = 0;
    return function () {
      return o >= r.length ? {
        done: !0
      } : {
        done: !1,
        value: r[o++]
      };
    };
  }
  throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
}
function _unsupportedIterableToArray(r, a) {
  if (r) {
    if ("string" == typeof r) return _arrayLikeToArray(r, a);
    var t = {}.toString.call(r).slice(8, -1);
    return "Object" === t && r.constructor && (t = r.constructor.name), "Map" === t || "Set" === t ? Array.from(r) : "Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t) ? _arrayLikeToArray(r, a) : void 0;
  }
}

var SphinxColorschemeImageHandler = function SphinxColorschemeImageHandler(options) {
  var _this = this;
  if (options === void 0) {
    options = {};
  }
  this.activate = function (scheme) {
    var data_att = "data-alt-src-color-scheme-" + scheme;
    var images = document.querySelectorAll("img[" + data_att + "]");
    var _loop = function _loop() {
      var img = _step.value;
      var new_img = new Image();
      var new_src = img.getAttribute(data_att);
      new_img.src = new_src;
      new_img.addEventListener('load', function () {
        img.src = new_img.src;
      });
      new_img.addEventListener('error', function () {
        console.error("Could not replace image " + img.src + " with " + new_src + ".");
      });
      if (new_img.complete) {
        img.src = new_img.src;
      }
    };
    for (var _iterator = _createForOfIteratorHelperLoose(images), _step; !(_step = _iterator()).done;) {
      _loop();
    }
  };
  this._schemes = [];
  this._mediaqs = [];

  // If options are not given or if it is given with a key 'auto'
  // and a boolean value true, then the instance created will add
  // an event listener for changes on prefers-color-scheme to
  // update images accordingly.
  this._auto = options.hasOwnProperty('auto') ? options['auto'] === true : true;
  var meta_prop = document.querySelector('meta[name="color-scheme"]');
  var meta_schemes = meta_prop != null ? meta_prop.content : "";
  if (meta_schemes.length > 0) {
    var schemes = meta_schemes.split(" ");
    for (var _iterator2 = _createForOfIteratorHelperLoose(schemes), _step2; !(_step2 = _iterator2()).done;) {
      var item = _step2.value;
      this._schemes.push(item.trim());
    }
  } else {
    this._schemes = ['light', 'dark'];
  }
  var _loop2 = function _loop2() {
    var scheme = _step3.value;
    var q = globalThis.matchMedia("(prefers-color-scheme: " + scheme + ")");
    if (q.matches) {
      _this.activate(scheme);
    }
    if (_this._auto === true) {
      q.addEventListener('change', function (e) {
        if (e.matches) {
          console.log('event:', e);
          _this.activate(scheme);
        }
      });
      _this._mediaqs.push(q);
    }
  };
  for (var _iterator3 = _createForOfIteratorHelperLoose(this._schemes), _step3; !(_step3 = _iterator3()).done;) {
    _loop2();
  }
};

export { SphinxColorschemeImageHandler };
//# sourceMappingURL=sphinx-colorschemed-images.esm.js.map