# Binary Ninja Plugins

Repository to track Binary Ninja Plugins, Themes, and other related tools

## Plugins

Binary Ninja plugins are available in different channels. Currently, there are two channels:

 - [Official](plugins/official): The official channel includes plugins written directly by [Vector 35](https://vector35.com/) or written by a third-party and verified by Vector 35. We have at least done our best to ensure they use the current plugin writing best-practices and provide useful functionality.

 - [Community](plugins/community): The community channel includes plugins written by third-parties that are not verified for quality, safety, or efficacy.  

 - [Combined](plugins/): A combined list of all plugins.

A [sample plugin](plugins/official/sample_plugin/) is available to demonstrate the required format for plugins.

### Installing Plugins

To install plugins, you can either clone this repository, or clone the specific plugin you are interested in and

### Contributing Plugins

 1. Create a new repository (Optionally, just copy it from the [sample plugin](plugins/official/sample_plugin/))
 1. Fill out a [`plugin.json`](/Vector35/binaryninja-plugins/blob/master/plugins/official/sample_plugin/plugin.json)
 1. (Optional) Run `generate-readme.md` to update your readme and license 
 1. Fork this repository
 1. Add your plugin as a submodule: `git submodule add https://github.com/YourName/YourPlugin plugins/community/YourPlugin`
 1. Regenerate the plugin directory with `generate-index.py`
 1. Commit and issue a [pull request](/Vector35/binaryninja-plugins/pull/new/master)

## License

Note that content contained in the root of this repository itself is Copyright 2016, Vector 35 LLC and [available](LICENSE) under an MIT license, but that each individual plugin may be released under a different license.
