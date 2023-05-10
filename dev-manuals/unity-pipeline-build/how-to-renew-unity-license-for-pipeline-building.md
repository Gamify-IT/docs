# How to renew unity license for pipeline building

The current Unity student license expires on 13.05.2024. Until then, it can be used for the pipeline build of Overworld & Chickenshock without any problems. After that, the following steps must be taken to apply for and deposit a new license, otherwise the pipeline build of Overworld & Chickenshock will no longer work:

1) Open https://unity.com/products/unity-student
1) Click "Get started" below "Post-secondary students"
1) Sing into your or create a new Unity account
1) Fillout the form & verify at SheerId that you are a student
1) You will receive an email with your license key
1) Open https://github.com/Gamify-IT
1) Goto Settings -> Secrets and variables -> Actions
1) Replace the `UNITY_EMAIL` secret with your unity account email-adress
1) Replace the `UNITY_LICENSE` secret with the license key you got per mail
1) Replace the `UNITY_PASSWORD` secret with your unity account password
1) Update this documentation with the new expiration date
1) Your done!