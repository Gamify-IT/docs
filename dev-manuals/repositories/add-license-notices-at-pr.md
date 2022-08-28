# How to check, add and update license notices at every PR

If you add or update a dependency it must be added to the third party license notice file before tomorrow.

To do that, you should add a new line like
```json
{"licTypeName": "MIT", "compName": "UniTask", "compVersion": "2.3.1", "copyright": "Copyright (c) 2019 Yoshifumi Kawai / Cysharp, Inc.", "copyrightSource": "https://github.com/Cysharp/UniTask/blob/2.3.1/LICENSE"}
```
to <https://github.com/Gamify-IT/third-party-license-notice/blob/main/LicenseNotes.json>.

If a license is used that we have not used before, it must be added to [this file](https://github.com/Gamify-IT/third-party-license-notice/blob/main/Licenses.json) as follows: `{"licTypeName": "MIT", "licText": "Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."},
`