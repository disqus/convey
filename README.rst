convey
======

This project is in development, and should be considered a prototype on an idea.

The goal is to add descriptive context around tests, so that you can easily and quickly
show what is going on without writing docstrings (which provides some other semi-benefits).

[Proposed] Features:

- Describe test classes (what are they testing)
- Describe test functions (what are they asserting)
- Memoize fixtures
- Improved output

Adding desciptive context to your test cases would look something like this::

::

    @describe(Forum)
    class Test:
        # ^^ we're not inheriting from anything, but thats ok because we'll inject unittest2.TestCase

        @fixture
        def forum(self):
            return Forum(id=1, url='demo')

        @should('have an id of 1')
        def test(self):
            self.assertEquals(self.forum.id, 1)

        @should('have a url of demo')
        def test(self):
            self.assertEquals(self.forum.url, 'demo')

        # Not sure if we'd really make nesting a possibility, but could be cool
        # (implied inheritence, so you'd get non-tests, like fixtures)
        @describe(Forum.get_url)
        class Test:

            @should('return the url')
            def test(self):
                self.assertEquals(self.forum.get_url(), 'demo')

The output would be improved when using verbosity > 1::

    disqus.forums.models.Forum
        should have an id of 1: passes
        should have a url of demo: passes

        from_url
            should return the url: failed!
