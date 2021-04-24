from flask import Flask, render_template, request, redirect
from google.cloud import datastore
from datetime import datetime

app = Flask(__name__)
db = datastore.Client()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/posts', methods = ['GET'])
def posts():
    """ Display all Posts """
    query = db.query(kind="Post", order=["-date_posted"])
    return render_template('posts.html', posts = query.fetch())


@app.route('/posts/add', methods = ['GET', 'POST'])
def posts_add():
    '''
    GET: Display a form to create Post
    POST: Save new Post
    '''
    if request.method == 'POST':
        post = datastore.Entity(db.key("Post"))
        post.update(
            {
                "title": request.form['title'],
                "content": request.form['content'],
                "author": request.form['author'],
                "date_posted": datetime.now()
            }
        ) 
        db.put(post)
        return redirect('/posts')
    else:
        return render_template('posts_form.html', post=None)


@app.route('/posts/edit/<int:id>', methods = ['POST', 'GET'])
def posts_edit(id):
    '''
    GET: Display a form to edit Post
    POST: Update Post
    '''
    post = db.get(db.key("Post", id))
    if request.method == 'POST':
        post["title"] = request.form["title"]
        post["author"] = request.form['author']
        post["content"] = request.form['content']  
        db.put(post)
        return redirect('/posts')
    else:
        return render_template('posts_form.html', post = post)


@app.route('/posts/delete/<int:id>', methods = ['GET'])
def posts_delete(id):
    ''' Delete Post '''
    db.delete(db.key("Post", id))
    return redirect('/posts')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

