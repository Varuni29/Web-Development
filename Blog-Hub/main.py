from flask import Flask,render_template
import requests
app=Flask(__name__)
blog_url = "https://api.npoint.io/890f95f5e71dc7a12390"
response=requests.get(blog_url)
posts=response.json()


@app.route('/')
def home():
    return render_template('index.html',all_posts=posts)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def get_blog(index):
    requested_post=None
    for particular_post in posts:
        if particular_post['id']==index:
            requested_post=particular_post
            if index==1:
                post_img="https://images.unsplash.com/photo-1516481605912-d34c1411504c?ixlib"
            elif index==2:
                post_img = "https://images.unsplash.com/photo-1606103920295-9a091573f160?ixlib"
            else:
                post_img = "https://images.livemint.com/img/2021/04/06/1140x641/Intermittent_fasting_1617685049521_1617704965248.jpg"
    return render_template("post.html",post=requested_post,imgs=post_img)

if __name__=="__main__":
    app.run(debug=True)