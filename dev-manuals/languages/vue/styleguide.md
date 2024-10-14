# Vue style guide

We are using the official [Vue Style Guide](https://vuejs.org/style-guide/#rule-categories).

## Script setup

Regarding script setup section in `.vue` files (newly introduced in Vue 3),
we are using the default TypeScript lint configuration included in Vue and Eslint.

## Configuration

The following configurations are used:
- `plugin:vue/vue3-essential` (included in vue)
- `eslint:recommended` ()
- `@vue/typescript/recommended`
- `plugin:prettier/recommended`

The projects use eslint with the following `.eslintrc.js` configuration file.

```javascript
module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ['plugin:vue/vue3-essential', 'eslint:recommended', '@vue/typescript/recommended', 'plugin:prettier/recommended'],
  parserOptions: {
    ecmaVersion: 2020,
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
  },
  overrides: [
    {
      files: ['**/__tests__/*.{j,t}s?(x)', '**/tests/unit/**/*.spec.{j,t}s?(x)'],
      env: {
        jest: true,
      },
    },
  ],
};

```
