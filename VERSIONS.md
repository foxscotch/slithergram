# Versions

I'm going to _try_ to use [Semantic Versioning][semver], but who knows if it'll
work out. This is kinda small, so I normally wouldn't consider versioning all
that necessary, but given that it'll probably map pretty closely to the official
Telegram API, which definitely uses version numbers, I think I should probably
do the same, for dependency reasons.

[semver]: http://semver.org/

Note: This is just for keeping up with changes, _not_ for documenting the API.

Here's how it's gonna go:

```markdown
## MAJOR

### MINOR

#### PATCH
```

Got it? Okay.


## 0.x.x


### 0.0.x


#### 0.0.2

- Fixed a bug with Bot.update_info(). It used the base_url attribute rather than
  just url, leading to it retrieving a plain web page, causing a JSONDecodeError


#### 0.0.1

- Replaced the messy contents of the `else` block in Bot.__init__() with a call
  to Bot.update_info()
- Added '.pkl' file extension to default filename for Bot.serialize_to_file()


#### 0.0.0

This is the first version. I'm not really _sure_ if it's supposed to start with
all zeroes, but it gets the job done. Since there aren't any changes to list, I
might as well just make a quick description of what I made before starting this.

- Bot class in slithergram.bot
    - `base_url`
    - `__init__()`
    - `__repr__()`
    - `__str__()`
    - `update_info()` (now that I think about it, `__init__()` should probably call this)
    - `serlialize_to_string()`
    - `serlialize_to_file()`
    - `deserlialize_from_string()`
    - `deserlialize_from_file()`
- example_bot Bot instance in slithergram.bot, just an example. I'll probably
  get rid of it later, or comment it out, or something.