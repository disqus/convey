convey
======

This project is in development, and should be considered a prototype on an idea.

::

    @describe(Forum)
    class Test:

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

