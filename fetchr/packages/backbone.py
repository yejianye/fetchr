from fetchr.packages.base import package, SimplePackage

@package
class Underscore(SimplePackage):
    """Utility-belt library that provides a lot of functional programming support."""
    version = '1.4.3'
    @property
    def cdn_urls(self):
        return ['//cdnjs.cloudflare.com/ajax/libs/underscore.js/$version/underscore-min.js']

    @property
    def dev_urls(self):
        return ['http://underscorejs.org/underscore.js']

    @property
    def min_urls(self):
        return ['http://underscorejs.org/underscore-min.js']

@package
class Backbone(SimplePackage):
    """Micro-framework gives structure to web applications by providing model/collection/view.""" 
    version = '0.9.10'
    deps = ['underscore']
    @property
    def cdn_urls(self):
        return ['//cdnjs.cloudflare.com/ajax/libs/backbone.js/$version/backbone-min.js']

    @property
    def dev_urls(self):
        return ['http://backbonejs.org/backbone.js']

    @property
    def min_urls(self):
        return ['http://backbonejs.org/backbone-min.js']

