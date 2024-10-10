# Code Format for TS

We use [ESLint](https://eslint.org/) for linting TS Code.  
We use [ESLint Vue Plugin](https://eslint.vuejs.org/) for linting Vue files.  
We use [Prettier](https://prettier.io/) for formatting TS Code.  
Please include them as a dev dependency in frontend projects:

```bash
npm install --save-dev prettier eslint eslint-plugin-vue
```

## Customizing Prettier

Prettier uses 80 chars per line and double quotes by default.
You should manually increase this to `130` and use single quotes by calling the following in the project root directory:

```bash
echo "{\"singleQuote\": true,\"printWidth\": 130}">.prettierrc.json
```
