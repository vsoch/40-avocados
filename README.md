# 40 Avocados

[![CircleCI](https://circleci.com/gh/vsoch/40-avocados.svg?style=svg)](https://circleci.com/gh/vsoch/40-avocados)

Apple recently announced the return of their Apple (colorful!) logo from the 
days of old school. And it's only available for $40.00 "exclusively at the Flag Park Visitor's Center,"
as announced on [Hackaday](https://hackaday.com/2018/10/30/apple-introduces-what-weve-all-been-waiting-for/).

Wait, did I hear that right? $40.00 for a T-Shirt? Are you *mad* ?

You know what I'd rather use $40.00 for? Just about anything else. Especially 
something I can eat. Like [40 avocados](https://vsoch.github.io/40-avocados).

## What can I get for $40.00?
What other N things could you get, instead of a T-shirt? [Open a pull request](https://www.github.com/vsoch/40-avocados/pulls) to add an image to the list by just adding an entry to the [things.yml](things.yml) file. What does this mean?
Here is an example:

```yaml
  avocados:
    - number: 40
    - image: https://vsoch.github.io/assets/images/posts/truelove/avocado.png
    - link: https://vsoch.github.io/2018/truelove/
  apple:
    - number: 1
    - image: https://hackadaycom.files.wordpress.com/2018/10/applerainbowlogoheader.jpg?w=800
    - link: https://hackaday.com/2018/10/30/apple-introduces-what-weve-all-been-waiting-for/
```

The first entry is for "avocados" meaning that the final web address will be 
[https://vsoch.github.io/40-avocados/avocados](https://vsoch.github.io/40-avocados/avocados). I am 
generating metadata for the number of things (number is 40), the image  want to use (and make sure you are
able to do this (image) and the link I want my images to go to.

When you open a pull request,  it will generate the site on CircleCI, and the site will be deployed
on merge! [Here](https://vsoch.github.io/40-avocados). is the deployment if you are interested. Have fun!

> I choose avocados

  - **Sid the avocado Sloth**
