# Write Poetry

This Docker recipe will use the [things.yml](../things.yml) from this repository
to write... the 12 Days of Halloweenie! You can generate just text, or markdown.
Give it a try!

## Text

```bash
$ docker run vanessa/40-avocados
On the 128 day of Halloweenie my pusheena earthworm gave to me, ... dumplings
On the 60 day of Halloween my stanky despacito gave to me, ... rainbow-glasses
On the 40 day of October my fugly blackbean gave to me, ... avocados
On the 36 day of Hacktoberfest my chunky spoon gave to me, ... kitkats
On the 28 day of Halloween my butterscotch gato gave to me, ... white-bread
On the 26 day of Fall my swampy blackbean gave to me, ... jet-puffed-marshmallows
On the 24 day of Hacktoberfest my strawberry arm gave to me, ... nike-socks
On the 20 day of Halloweenie my peachy egg gave to me, ... espresso
On the 8 day of October my dirty pumpkin gave to me, ... waving-cats
On the 5 day of Hacktoberfest my phat parsnip gave to me, ... canned-unicorn-meat
On the 2 day of Fall my orange house gave to me, ... the-elder-scrolls-online
And arduino-mkr-zero just for me :)
```

## Markdown
And now markdown!

```bash
$ docker run vanessa/40-avocados markdown
```

 - On the 240 day of Fall my red noodle gave to me, ... [240 pencils](https://vsoch.github.io/40-avocados/pencils)
 - On the 128 day of Fall my tart frito gave to me, ... [128 dumplings](https://vsoch.github.io/40-avocados/dumplings)
 - On the 36 day of Halloweenie my persnickety animal gave to me, ... [36 kitkats](https://vsoch.github.io/40-avocados/kitkats)
 - On the 28 day of Halloweenie my confused signal gave to me, ... [28 white bread](https://vsoch.github.io/40-avocados/white-bread)
 - On the 24 day of Halloweenie my loopy punk gave to me, ... [24 nike socks](https://vsoch.github.io/40-avocados/nike-socks)
 - On the 23 day of Halloweenie my wobbly caramel gave to me, ... [23 fidget spinner toy](https://vsoch.github.io/40-avocados/fidget-spinner-toy)
 - On the 20 day of Hacktoberfest my conspicuous poodle gave to me, ... [20 espresso](https://vsoch.github.io/40-avocados/espresso)
 - On the 10 day of Hacktoberfest my fugly leopard gave to me, ... [10 pumpkins](https://vsoch.github.io/40-avocados/pumpkins)
 - On the 8 day of Halloween my swampy latke gave to me, ... [8 waving cats](https://vsoch.github.io/40-avocados/waving-cats)
 - On the 5 day of October my arid peanut-butter gave to me, ... [5 canned unicorn meat](https://vsoch.github.io/40-avocados/canned-unicorn-meat)
 - On the 4 day of October my arid rabbit gave to me, ... [4 justin bieber purpose audio cd](https://vsoch.github.io/40-avocados/justin-bieber-purpose-audio-cd)
 - And [a 1 morgan silver dollar](https://vsoch.github.io/40-avocados/morgan-silver-dollar) just for me :)

Have fun!

## Development

Since this container doesn't need changing largely (the content comes from the things.yml online
it is a manual build and push!

```bash
docker build -t vanessa/40-avocados .
docker tag vanessa/40-avocados vanessa/40-avocados:0.0.2
docker push vanessa/40-avocados
```
