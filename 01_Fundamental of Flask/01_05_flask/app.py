from flask import Flask, render_template
from models import ArticleModel

apps = Flask(__name__)

content = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis lobortis turpis et mi interdum, nec convallis nisi fermentum. Cras justo libero, condimentum quis mauris ac, euismod sollicitudin sem. Sed eget tincidunt lorem, ac volutpat metus. Fusce urna ex, sollicitudin ut scelerisque nec, maximus in ante. Duis ut blandit mauris. Morbi egestas malesuada porttitor. Ut euismod, enim at rhoncus ultrices, tellus tortor consectetur tellus, id ultricies nulla dui nec tellus. Cras velit elit, dignissim at feugiat eu, auctor ac purus. Curabitur tincidunt, est vitae euismod sodales, augue purus lobortis nibh, at finibus ligula justo vel dolor. Praesent sed suscipit neque. Vivamus dictum ante sed leo vulputate, dapibus vulputate sem rutrum. Maecenas mattis sed eros vulputate pharetra. Vivamus rhoncus ornare accumsan. Duis nisi ligula, egestas at sodales ut, viverra ac nunc.
'''

@apps.route('/')
def index():
    # create object from ArticleModel Class
    model = ArticleModel()
    
    # fill value to model
    model.setTitle('What is Lorem Ipsum ?')
    model.setDate('16/04/2022')
    model.setContent(content)
    
    # send nilai to view
    return render_template('article.html',
            title=model.getTitle(),
            date=model.getDate(),
            content=model.getContent())
            
            
    
if __name__ == '__main__':
    apps.run(debug=True)
    