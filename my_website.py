import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu

st.set_page_config(page_icon="π", page_title="Our Life", layout="wide")
st.experimental_memo.clear()
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
vert_space = """
                <style>
                .appview-container .main .block-container{padding-top: 1rem;}
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o10 > div.css-6qob1r.e1fqkh3o3 > div.css-hxt7ib.e1fqkh3o4
                {padding:1rem}
                 #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o10 > div.css-6qob1r.e1fqkh3o3 > div.css-1xtoq5p.e1fqkh3o2 > button
                  {display: none;}
                  #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o10 > div.css-6qob1r.e1fqkh3o3
                  {background-color:white}
                </style>
                """
st.markdown(vert_space, unsafe_allow_html=True)
# 1. as sidebar menu
with st.sidebar:
    selected = option_menu(
        # "Our Life"
        None
        , ["ε°ι’","δΈζε²", 'ιιε¬ε­','εθ₯'],
        icons=[None,'dot', 'dot','dot']
        , menu_icon="cast"
        , default_index=0
    ,styles = {
        "container": {"padding": "0!important"},
        "icon": {"color": "grey", "font-size": "10px"},
        "nav-link": {"color":"#333333","font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "transparent"},
        "nav-link-selected": {"color":"black","font-weight": "bold","background-color": "transparent"},
    }

    )

if selected=="ε°ι’":
    back_color = """
                    <style>
                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3
                      {background:beige}
                    </style>
                    """
    st.markdown(back_color, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.header("**ηζ΄»θ?°ε½ε**")
        st.write("""
        *θΏζ―ι­ε½©η₯εθ’ηηθ?°ε½ε* \n
        *this is our life*
        """)

    with col2:
        st.image("https://www.hepuhua.cn/zb_users/upload/2020/01/20200107161419_14086.jpeg")
if selected=="δΈζε²":
    back_color = """
                    <style>
                    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3
                      {background:white}
                    </style>
                    """
    st.markdown(back_color, unsafe_allow_html=True)

    pics_path = ["https://c2.im5i.com/2022/10/21/TxPSO.jpg",
                 "https://c2.im5i.com/2022/10/21/Txd8d.jpg",
                 "https://c2.im5i.com/2022/10/21/TxGDy.jpg",
                 "https://c2.im5i.com/2022/10/21/TxVuR.jpg",
                 ]

    pic_html = ""
    for i, path in enumerate(pics_path):
        if i == 0:
            pic_html += """
                <div class="item active">
            			<img src=\"""" + path + """\">
            			<div class="carousel-caption"></div>
            		</div>
                """
        else:
            pic_html += """
            <div class="item">
                    <img src=\"""" + path + """\">
                    <div class="carousel-caption"></div>
                </div>
            """
    data = """
    <!DOCTYPE html>
    <html>
    <head>
    	<meta charset="utf-8">
    	<title>Bootstrap ε?δΎ - θ½?ζ­οΌCarouselοΌζδ»Άηζ ι’</title>
    	<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
    	<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
    	<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <body>

    <div id="myCarousel" class="carousel slide">

    	<!-- θ½?ζ­οΌCarouselοΌι‘Ήη? -->
    	<div class="carousel-inner">
    """ + pic_html + """
    	</div>
    	<!-- θ½?ζ­οΌCarouselοΌε―Όθͺ -->
    	<a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
    	    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    	    <span class="sr-only">Previous</span>
    	</a>
    	<a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
    	    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    	    <span class="sr-only">Next</span>
    	</a>
    </div>

    </body>
    </html>
    """

    html(data, height=500,width=888, scrolling=False)
    st.write(" ")
    st.write(" ")
    st.write("""
    *θΏιζ―**δΈζε²**οΌδΈ­ε½ζδΈζΉηε°ε²οΌη¬¬δΈηΌι³εη§ε°ηε°ζΉγ
    text text text text text text text text text text tex*
    """
    )
if selected=="ιιε¬ε­":
    back_color = """
                    <style>
                      # root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3
                      {background-color:white}
                    </style>
                    """
    st.markdown(back_color, unsafe_allow_html=True)

    st.write("""
    *θΏιζ―ζζ¬οΌζδ»¬θ¦ε¨θΏιεδΈθ―θ―­γ*
    """)
    pics_path=["https://www.hepuhua.cn/zb_users/upload/2020/01/20200107161419_14086.jpeg"
               ,"https://tse4-mm.cn.bing.net/th/id/OIP-C.QvaILHSh2n_V9Hy97GZoCgHaJF?pid=ImgDet&rs=1"
               ,"https://tse1-mm.cn.bing.net/th/id/OIP-C.-P1PBsUfbQtjmK1M_wE7jAHaGB?pid=ImgDet&rs=1"
               ,"https://p1.ssl.qhimg.com/t0195dfff9acc0d6ac3.jpg"
               ,"https://pic1.zhimg.com/v2-c11ed3406da42746c651e5a15a3f8a40_r.jpg"]
    col1, col2 ,col3= st.columns(3)
    with col1:
        for i,path in enumerate(pics_path):
            if i%3 ==0:
                st.image(path,use_column_width=True)
    with col2:
        for i,path in enumerate(pics_path):
            if i%3 ==1:
                st.image(path,use_column_width=True)
    with col3:
        for i, path in enumerate(pics_path):
            if i % 3 == 2:
                st.image(path, use_column_width=True)


