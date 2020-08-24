# FreeTranslate
![Screenshot of FreeTranslate](https://kevinmichaelloeffler.files.wordpress.com/2020/08/after.png)

Amazon Web Services has a product called Amazon Translate which is a neural machine translation service, meaning it translates text using machine learning. It is very powerful, and while it cannot replace a human translator, can help people like teachers convey meaning to the communities they work with reliably. Unfortunately this tool is intended for developers, whereas it can be of great value to people who are not programmers. It also has a generous free tier of usage, letting you translate 2 million characters per month for 12 months at no cost.

That’s where FreeTranslate comes in. FreeTranslate is a software project I have worked on that allows people to deploy a personal translation page to use these free credits by simply clicking a button. It will deploy FreeTranslate to your Amazon account and generate a personal URL just for you!

The technical details are that I have build a CloudFormation template that deploys when you click a URL on my projects page. This template deploys an API Gateway (for the webpage and sending translation requests) and a Lambda function (which does the actual translation bit).

[You can deploy this tool with one click and see additional pictures and instructions here!](https://kevinmloeffler.com/projects/freetranslate/)
