'use strict';

const path = require('node:path');
const process = require('node:process');
const { babel } = require('@rollup/plugin-babel');
const { nodeResolve } = require('@rollup/plugin-node-resolve');
const replace = require('@rollup/plugin-replace');
const getBanner = require('./banner.js');

const ESM = process.env.ESM === 'true';
const UMD = process.env.UMD === 'true';
const build_module = (ESM || UMD);
const suffix = ESM ? "esm" : "umd";

const input_module = path.resolve(__dirname, "src/main.js");
const input_script = path.resolve(__dirname, "src/script.js");
const output_module = path.resolve(
  __dirname, `../dist/js/sphinx-colorschemed-images.${suffix}.js`
);
const output_script = path.resolve(
  __dirname,
  '../sphinx_colorschemed_images/',
  'static/sphinx-colorschemed-images.js'
);

const plugins = [
  babel({
    exclude: 'node_modules/**',
    babelHelpers: 'bundled'
  }),
];

if (!ESM) {
  plugins.push(
    replace({
      'process.env.NODE_ENV': '"production"',
      preventAssignment: true
    }),
    nodeResolve()
  );
}

const config = {
  input: build_module ? input_module : input_script,
  output: {
    banner: getBanner(),
    file: build_module ? output_module : output_script,
    format: ESM ? 'esm' : 'umd',
    generatedCode: 'es2015',
  },
  plugins
};

if (UMD) {
  config.output.name = 'sphinx_colorschemed_images';
}

module.exports = config;