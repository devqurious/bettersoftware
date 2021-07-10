      
---
title: Validate your inputs
date: 2021-06-10T19:37:38.262Z
thumb_image: /images/input_validation.jpg
omit_header_text: "true"
draft: "false"
summary: Error. That password is already used by StarBoy98
tags:
  - Software Development
categories:
  - Blogs
---

![](/images/input_validation.jpg)

"*Error. That password is already used by StarBoy98.*"

Yes, this is one of the jokes doing the rounds of the Internet on validation taken to the extreme. However, lack of validation is often the main reason contributing either to a bad user experience, or worse, a security breach. 

A common problem when estimating the time it would take to complete a story is to only consider the “happy path.” The user enters the email address correctly, uploads the certificate in the right format, and of course, the user is entering the form using the queen’s English language, right? 

### Stored XSS

Without input validation, hackers can attack your application using cross-site scripting. To launch a cross site attack, abbreviated as XSS, the attacker visits your site and places some JavaScript code into your database using one of your un-validated form fields, for example, your "Add a comment" field. Now that JavaScript code will be downloaded, as a "comment", by all users that visit your blog page.

Why is this bad? 

Well, as soon as the browser downloads the JavaScript code, the next thing it does is run it. The attacker can craft the JavaScript code to steal cookies for your web application. Now, the attacker can present those cookies to your web application and boom - he or she is in as a "legit" user. It all goes south from here.

 Validation is your defense. In addition to validation done at the front-end (the UI layer), separate validation is needed in the back end layer as well. The back end should not assume the data is validated properly by the front end for two reasons. First - you may some day expose your back end directly via API’s. And second, hackers don’t come in through your UI. The will curl in to your back end directly. 
 
### What should you validate?
 
 Does your input need only a specific set of characters? Then limit the input to only allow those characters - that's a good first step. 
 
 Place a size limit on the inputs where you can - for example, input fields like name, address can be bound to maximum size in terms of number of characters they can hold.
 
 If the input is of a special type, like an IP address or MAC address, you can perform even better validation using regular expressions because you know the precise data format.
 
 Check for blank inputs. 

### Validation checklist
 Often times, input validation is the bulk of the code. If you don’t plan for it initially, then it may result in a number of bugs being found later on which could throw your schedule out of whack.
 
 Remember:
 
 - [ ] Strict validation is your best defense against bad actors.
 - [ ] Perform validation in the frontend (UI) _and_ in the backend. 
 - [ ] Run tools like SonarQube that will alert you when un-validated code is found. 
 - [ ] A pull request (PR) checklist should include validation as one of it's items.
 - [ ] Story estimates should include "un-happy" path validaton.