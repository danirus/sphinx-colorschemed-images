'use strict';

const path = require('node:path');
const process = require('node:process');
const { babel } = require('@rollup/plugin-babel');
const { nodeResolve } = require('@rollup/plugin-node-resolve');
const replace = require('@rollup/plugin-replace');
const getBanner = require('./banner.js');

const ESM = process.env.ESM === 'true';

const input_module = path.resolve(__dirname, "src/main.js");
const input_script = path.resolve(__dirname, "src/script.js");
const output_module = path.resolve(
  __dirname, `../dist/js/sphinx-colorschemed-images.esm.js`
);
const output_script = path.resolve(
  __dirname, `../dist/js/sphinx-colorschemed-images.js`
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
  input: ESM ? input_module : input_script,
  output: {
    banner: getBanner(),
    file: ESM ? output_module : output_script,
    format: ESM ? 'esm' : 'umd',
    generatedCode: 'es2015',
  },
  plugins
};

if (!ESM) {
  config.output.name = 'sphinx-colorschemed-images';
}

module.exports = config;