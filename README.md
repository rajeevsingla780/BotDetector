# BotDetector
Due to increasing use of internet services there has been an increase in the
threat to security. As a result, some systems named CAPTCHA (Completely Automated Public
Turing test to tell Computers and Human Apart) have been introduced to tell apart human users
and bots. Unfortunately, the use of a CAPTCHA limits the accessibility of a website, as some
Software Requirements Specification for Bot Detector for Blind 5
tests can be difficult for certain users to perform. 


In the case of visual CAPTCHAs, visually
impaired web users are particularly disadvantaged. Site operators must therefore decide whether
adoption of a CAPTCHA is appropriate for their application, weighing the relative benefits of
automated access prevention and accessibility. Some sensitive applications, such as online
banking, may warrant stringent safeguards against automated access at the sake of accessibility,
while other applications, for instance public loges or forums, may not want to inhibit user
participation by incorporation of a CAPTCHA.


The visually impaired people will be able to access captcha secured forums and websites which
are not offered to them currently.This software can provide an edge over the captcha already in
use. The main advantage of our software is to help limit spam, especially from automated
programs that send email, submit web forms and create online accounts. Implementing this type
of CAPTCHA to the existing website is also very simple. Thus, making it ideal for software
developers to use. It combines many features like random number generator, text to speech, hand
gesture detection & recognition. 

#  Requirements
Chrome Extension- ChromeVox Classic Extension
Link: https://chrome.google.com/webstore/detail/chromevox-classic-extensi/kgejglhpjiefppelpmljglcjbhoiplfn/related?hl=en

Background should not be noisy ,It should be clear upto 40 percent noice ratio

# The major features of product are as follows
## Random Number Generator
Random Number generator is responsible for generating 4 random numbers each out of
range [0,4] both included. These random numbers are the base of the software and
responsible for all the activities ahead.
## Text to Speech
The Random Number so generated is then converted to speech using an API for the
convenience of the users. The speech so heard by the user will be performed as gestures with
his/her hand.
## Gesture Detection
The Gestures performed by the user are captured as Images, preprocessed and further computations are performed.
## Gesture Recognition
The images are compared with the generated random number and a final result is obtained
where we get a decision whether a user is a bot or not. If bot is detected then will be
redirected to the reCAPTCHA where the whole process restarts. Otherwise, the form is
submitted successfully.
