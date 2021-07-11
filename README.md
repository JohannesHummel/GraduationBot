# GraduationBot
This Bot supports the User in scientific writing. It can help the User with the following tasks:
- Search for Papers of certain Topics
- Answering questions about latex in general
- Get information regarding seminars 
- Help the User find a topic for a thesis or help finding a professor

### Installation
You can run the Rasa part of the Bot separately from Discord.
First setup Rasa on your PC:

`pip3 install rasa`

Then you need to install `habanero`. A python version of the [crossref api](https://github.com/sckott/habanero) (needed for the paper search feature of the bot):

`pip3 install habanero`

You can run Rasa on the commad line with:

`rasa shell`

In another Terminal you should start the `rasa action server`:

`rasa run actions`

Now you can interact with the bot on the terminal without starting the discord bot.


### Functionality

This Bot supports the following questions from the User (can be asked in a different fashion, these are just example questions):
- What are your functions?

- How can I write text in italic?

- How can I write text in bold?

- How can I create a list in latex?

- Can you help me find a paper?

- What is Latex?

- How can I find a topic for my seminar?

- Where can I find Information regarding a thesis?
