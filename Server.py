import web

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self):
         filename=self.recv()

        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
