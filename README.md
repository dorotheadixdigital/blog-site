# Instructions

This week, you will be in a team of three or four people working on a project. You should use [GitHub issues](https://guides.github.com/features/issues/) to keep track of who is working on what, and should use [feature branches](https://bocoup.com/blog/git-workflow-walkthrough-feature-branches) for development.

Your team's creativity and common sense should be used as you work. There are common features to web applications that users expect. If they are not mentioned in the project's description, you should still do them. For example: in the Question Box application, users should have avatar images. You don't have to handle file uploads yourself -- you could use Gravatar with [django-gravatar](https://github.com/twaddington/django-gravatar) -- but you need some way of handling that.

Likewise, come up with your own features to make your project unique. You will likely use this project in your portfolio, so make it stand out!

## Trying new things

Each team should try something they don't know how to do on their project. This could be a Python or JavaScript library they haven't used before or a feature of Django they haven't tried.

Some ideas:

* [Allow users to authenticate via Google or other third-party auth](https://www.intenct.nl/projects/django-allauth/)
* [Try Dragula for drag and drop](https://bevacqua.github.io/dragula/)
* [Use Restless to build an API](https://restless.readthedocs.io/en/latest/)

# The Projects



## Project 2: QuestionBox

You want to make an application where people can crowdsource their questions and get answers. You are going to build a web application that has these goals:

* Users can view questions and answers
* Registered users can ask questions
* Registered users can add answers to any question
* The question's creator can mark answers as correct
* Registered users can "star" questions and answers they like

### How questions and answers work

Questions have a title and a body. Allow your users to use [Markdown](https://en.wikipedia.org/wiki/Markdown) for authoring question bodies. [Python-Markdown](https://python-markdown.github.io/) can turn Markdown into HTML for you. You will also want to prevent people from putting unauthorized HTML into your Markdown code. Using [Bleach](https://bleach.readthedocs.io/en/latest/clean.html) and [bleach-whitelist](https://github.com/yourcelf/bleach-whitelist) should help with that. Questions cannot be edited once they have been asked. A question can be deleted by its author. If it is deleted, all associated answers should also be deleted.

Answers just have a body and are connected to a question. Answers can also use Markdown.

Every question and every answer should be associated with a user.  A user should be able to view all their questions on a user profile page.

When a user answers a question, the question's author should receive an email with a link to the answer.

### How much of this is JavaScript and Ajax?

Adding answers should happen in the page with no page load, thereby needing Ajax. Likewise, "starring" questions and answers and marking answers as correct should happen via Ajax.

The rest of the application can be plain old Django views, although you can use JavaScript and Ajax to load questions and answers if you want.


