import { fixupConfigRules } from "@eslint/compat";
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
  ignores: ["build/*", "dist/js/*.js", "dist/js/*.js.map"],
}, ...fixupConfigRules(compat.extends(
  "plugin:import/errors",
  "plugin:import/warnings",
  "plugin:unicorn/recommended",
)), {
  rules: {
    indent: ["error", 2, {
      MemberExpression: "off",
      SwitchCase: 1,
    }],

    "max-len": ["error", {
      code: 80,
      comments: 72,
      ignoreUrls: true,
      ignoreRegExpLiterals: true,
      tabWidth: 2,
    }],

    "object-curly-spacing": "off",
    "unicorn/expiring-todo-comments": "off",
    "unicorn/prefer-module": "off",
    "unicorn/prefer-query-selector": "off",
    "unicorn/prevent-abbreviations": "off",
  },
}];
