import path from "node:path";
import { fileURLToPath } from "node:url";
import js from "@eslint/js";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all
});

export default [{
  ignores: ["coverage/*"],
}, ...compat.extends("../.eslintrc.json"), {
  languageOptions: {
    globals: {},
    ecmaVersion: "latest",
    sourceType: "module",
  },
}, {
  files: ["./src/**/*.js"],

  rules: {
    "import/extensions": [2, {
      js: "always",
      json: "always",
    }],
  },
}];
