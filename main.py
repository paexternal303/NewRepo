from blog.models import BlogPost
from blog.views import render_post

if __name__ == "__main__":
    post = BlogPost("Hello", "This is a post about blogging.")
    print(render_post(post))

        def add_tag(self, tag):
            self.tags.append(tag)
            self.author = author

