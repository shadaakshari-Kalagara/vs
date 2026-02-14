import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

# I KNOW YOU'D VISIT THIS REPO DHADIYAAAAAAA



st.set_page_config(
    page_title="V&S Hyd Journey 💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_image(image_path):
    import base64
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_base64 = get_base64_image("assets/photos/date1.jpg")

st.markdown(
    f"""
    <style>
        .stApp {{
            background:
                /* Top layer → main image */
                url("data:image/jpeg;base64,{bg_base64}") center / 76% no-repeat,

                /* Middle layer → tiny pink heart outlines */
                url("data:image/svg+xml,%3Csvg width='24' height='29' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M20 34s-9-6-14-11c-4-4-4-10 0-14 4-4 10-4 14 0 4-4 10-4 14 0 4 4 4 10 0 14-5 5-14 11-14 11z' fill='%23F8C8DC'/%3E%3C/svg%3E")
                /* Bottom layer → wine color */
                #4A001F;

            background-attachment: fixed;
        }}

        /* Title styling */
        .main-title {{
            text-align: center;
            color: white;
            font-size: 3.5em;
            font-family: 'Georgia', serif;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
            margin: 20px auto 30px;
            animation: fadeIn 1.5s;
            padding: 0 20px;
            max-width: 100%;
            z-index: 10;
        }}
                
        .sub-title {{
            background-color: #DFA7AC;
            padding: 1px;
            border-radius: 1px;
            text-align: center;
            color: brown;
            font-size: 1.3em;
            font-family: 'Georgia', serif;
            text-shadow: 3px 4px 6px rgba(0,0,0,0.4);
            margin: 10px auto 30px;
            animation: fadeIn 1.5s;
            padding: 0px 0px;
            width: 70%;
            z-index: 10;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* PERFECT BUTTON CENTERING - FIXED */
        .button-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            margin: 40px 0;
            padding: 0;
        }}

        /* Center the Streamlit button wrapper */
        div[data-testid="column"] {{
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }}

        .stButton {{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }}

        .stButton > button {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            font-size: 1.6em;
            padding: 25px 60px;
            border-radius: 50px;
            font-family: 'Georgia', serif;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
            transition: all 0.3s;
            width: auto;
            max-width: 500px;
            min-width: 350px;
            height: auto;
            line-height: 1.3;
            margin: 0 auto;
        }}

        .stButton > button:hover {{
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(245, 87, 108, 0.6);
            background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
        }}

        @media (max-width: 768px) {{
            .main-title {{
                font-size: 2.5em;
                margin-bottom: 20px;
            }}
            .stButton > button {{
                font-size: 1.4em;
                padding: 20px 40px;
                max-width: 90%;
                min-width: 280px;
            }}
        }}
    </style>
    """,
    unsafe_allow_html=True
)


HYD_LOCATIONS = [
    {
        "name": "Charminar",
        "x": 44.61,
        "y": 19.54,
        "image": "assets/photos/charminar.jpg",
        "letter": "Don't we both look amazing in white, We'll return to all these places someday chellom."
    },
    {
        "name": "Wayanad trip (Although not Hyd but still core memory)",
        "x": 56.26,
        "y": 48.62,
        "image": "assets/photos/Wayanad.jpg",
        "letter": "The one trip where we were inseparable and probably gave us an idea of how all of our future trips would be."
    },
    {
        "name": "Ikea date",
        "x": 57.93,
        "y": 59.04,
        "image": "assets/photos/ikea.jpg",
        "letter": "The one where we were hardly a month into dating and I knew I wanted a beautiful family and home with you. Ikea had me day dreaming coming home to beautiful furniture and the best husband on earth"
    },
    {
        "name": "Hard Rock Cafe",
        "x": 21.70,
        "y": 32.40,
        "image": "assets/photos/hardrock.jpg",
        "letter": "I'm drunk , you are sober and we still make an amazing pair. Can't wait to be crazy amount of crazy with you. I love how we always have alone moments even before we started dating and these moments led to us being together now"
    },
    {
        "name": "Midnight Icecreams with you ",
        "x": 51.57,
        "y": 62.88,
        "image": "assets/photos/Midnight Icecreams.jpg",
        "letter": "Just you and me, the scooty that only starts on my command, the cold breeze in our faces, me holding onto you tightly on the open roads....all leading to a delicious ice cream with my bestieee.(Please ignore the photo quality)"
    },
    {
        "name": "Bawarchi",
        "x": 32.45,
        "y": 48.01,
        "image": "assets/photos/bawarchi.jpg",
        "letter": "The best biryani tastes even better when shared with you. Every meal is a celebration with you."
    },
    {
        "name": "Home Sweet Home",
        "x": 36.45,
        "y": 58.01,
        "image": "assets/photos/homesweethome.jpg",
        "letter": "The moment I knew your'e the calm to my storm, yin to my yang and the best half not my better half."
    },
    {
        "name": "Tea to my coffee",
        "x": 88.45,
        "y": 52.01,
        "image": "assets/photos/tea to my coffee.jpg",
        "letter": "Let's argue for the rest of our lives which is better but deep down you know that coffee >>> tea (yuck)"
    },
    {
        "name": "Birthday",
        "x": 85.45,
        "y": 40.01,
        "image": "assets/photos/bday.jpg",
        "letter": "My man turned 24 y'all. I kinda like the fact that I am older than you hehe. Gimme some time Imma get you PS5 soon for your 26th hopefully"
    },
    {
        "name": "Skin care",
        "x": 74.61,
        "y": 19.54,
        "image": "assets/photos/skincare.jpg",
        "letter": "We looked low-key scary but cute couple stuff tho"
    },
    {
        "name": "Second Fancy Date",
        "x": 64.61,
        "y": 17.54,
        "image": "assets/photos/date2.jpg",
        "letter": "The candelight , my view and the food. Bestuhhhhhh. Lets continue our fancy dates with your Juliana"
    },
    {
        "name": "Happy Pista House date",
        "x": 24.61,
        "y": 17.54,
        "image": "assets/photos/pistah house.jpg",
        "letter": "Our go to place.Biriyani made us fall in love with each other and then the rest is history"
    },
    {
        "name": "Our fur child",
        "x": 86.61,
        "y": 17.54,
        "image": "assets/photos/our first child.jpg",
        "letter": "Brunolu also played a huge part of you and me getting together and my heart fills with joy whenever I see you both bonding.Also like dad like son hehe"
    }


]


if "current_page" not in st.session_state:
    st.session_state.current_page = "hyderabad"


def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        st.warning(f"Image load error ({image_path}): {str(e)}")
        return None


def create_interactive_map(locations, map_image_base64, heart_emoji="💖"):
    # Build popups HTML
    popups_html = ""
    for i, loc in enumerate(locations):
        photo_base64 = get_base64_image(loc['image'])
        if photo_base64:
            # Detect image type from filename for correct MIME type
            mime_type = "jpeg" if loc['image'].lower().endswith(('.jpg', '.jpeg')) else "png"
            photo_html = f'<img src="data:image/{mime_type};base64,{photo_base64}" class="popup-image" alt="{loc["name"]}">'
        else:
            photo_html = f'''
            <div style="padding: 60px; background: linear-gradient(135deg, #f5f7fa 0%, #C98A90 100%); 
                 border-radius: 20px; text-align: center; margin: 10px;">
                <p style="font-size: 4em; margin-bottom: 10px;">📸</p>
                <p style="font-size: 1.3em; color: #555; font-weight: 500;">{loc["name"]}</p>
                <p style="font-size: 1.1em; color: #777; margin-top: 8px;">Photo coming soon...</p>
            </div>
            '''
        
        popups_html += f'''
        <div id="popup-{i}" class="popup-overlay">
            <div class="popup-content">
                <button class="popup-close" onclick="closePopup({i})">×</button>
                <h2 class="popup-title">{loc['name']} 💕</h2>
                {photo_html}
                <p class="popup-letter">"{loc['letter']}"</p>
            </div>
        </div>
        '''
    

    hearts_html = ""
    for i, loc in enumerate(locations):
        x = max(3, min(97, loc['x']))
        y = max(3, min(97, loc['y']))
        hearts_html += f'''
        <div class="heart-pin" 
             style="left: {x}%; top: {y}%;" 
             onclick="showPopup({i})"
             title="{loc['name']}">
            {heart_emoji}
        </div>
        '''
    
    # Complete HTML with CSS and JavaScript
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Georgia', serif;
                background: transparent;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                width: 100%;
                overflow-x: hidden;
                padding: 20px;
            }}
            
            .map-container {{
                position: relative;
                width: 80%;
                max-width: 1200px;
                margin: 0 auto;
                border-radius: 20px;
                overflow: hidden;
                box-shadow: 0 15px 50px rgba(0,0,0,0.35);
            }}
            
            .map-container img {{
                width: 80%;
                opacity: 0.65;
                display: block;
                border-radius: 20px;
            }}
            
            .heart-pin {{
                position: absolute;
                font-size: 45px;
                cursor: pointer;
                transform: translate(-50%, -50%);
                transition: all 0.3s ease;
                filter: drop-shadow(0 0 10px rgba(255, 20, 147, 0.8));
                animation: heartbeat 1.5s infinite;
                z-index: 100;
                user-select: none;
            }}
            
            .heart-pin:hover {{
                font-size: 60px;
                animation: none;
                filter: drop-shadow(0 0 15px rgba(255, 20, 147, 1));
                z-index: 101;
            }}
            
            @keyframes heartbeat {{
                0%, 100% {{ transform: translate(-50%, -50%) scale(1); }}
                50% {{ transform: translate(-50%, -50%) scale(1.15); }}
            }}
            
            .popup-overlay {{
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.88);
                z-index: 9999;
                overflow-y: auto;
                padding: 20px;
                justify-content: center;
                align-items: center;
            }}
            
            .popup-overlay.show {{
                display: flex !important;
                animation: fadeIn 0.3s;
            }}
            
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            
            .popup-content {{
                background: pink;
                padding: 40px;
                border-radius: 25px;
                max-width: 700px;
                width: 65%;
                max-height: 60vh;
                overflow-y: auto;
                position: relative;
                animation: slideUp 0.4s;
                box-shadow: 0 25px 70px rgba(0,0,0,0.6);
            }}
            
            @keyframes slideUp {{
                from {{ transform: translateY(50px); opacity: 0; }}
                to {{ transform: translateY(0); opacity: 1; }}
            }}
            
            .popup-close {{
                position: absolute;
                top: 15px;
                right: 20px;
                font-size: 42px;
                cursor: pointer;
                color: #888;
                background: none;
                border: none;
                padding: 5px 12px;
                transition: all 0.3s;
                font-weight: bold;
                line-height: 1;
                z-index: 10;
            }}
            
            .popup-close:hover {{
                color: #ff1744;
                transform: scale(1.3);
            }}
            
            .popup-title {{
                color: #764ba2;
                font-size: 2.4em;
                margin-bottom: 30px;
                text-align: center;
                font-weight: bold;
                padding: 0 10px;
            }}
            
            .popup-image {{
                width: 100%;
                border-radius: 15px;
                margin-bottom: 30px;
                box-shadow: 0 6px 20px rgba(0,0,0,0.25);
            }}
            
            .popup-letter {{
                font-size: 1.35em;
                line-height: 1.8;
                color: #222;
                font-style: italic;
                text-align: center;
                padding: 30px;
                background: linear-gradient(135deg, #fff9fb 0%, #f0f7ff 100%);
                border-radius: 15px;
                border-left: 6px solid #764ba2;
                margin-top: 10px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            }}
            
            @media (max-width: 768px) {{
                .heart-pin {{
                    font-size: 38px;
                }}
                .heart-pin:hover {{
                    font-size: 48px;
                }}
                .popup-content {{
                    padding: 25px 20px;
                    margin: 15px;
                }}
                .popup-title {{
                    font-size: 1.8em;
                }}
                .popup-letter {{
                    font-size: 1.15em;
                    padding: 22px;
                }}
                .map-container {{
                    border-radius: 15px;
                }}
                .popup-close {{
                    font-size: 36px;
                    top: 10px;
                    right: 15px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="map-container">
            <img src="data:image/png;base64,{map_image_base64}" alt="Map">
            {hearts_html}
        </div>
        
        {popups_html}
        
        <script>
            function showPopup(locationId) {{
                const popup = document.getElementById('popup-' + locationId);
                if (popup) {{
                    popup.classList.add('show');
                    document.body.style.overflow = 'hidden';
                }}
            }}
            
            function closePopup(locationId) {{
                const popup = document.getElementById('popup-' + locationId);
                if (popup) {{
                    popup.classList.remove('show');
                    document.body.style.overflow = 'auto';
                }}
            }}
            
            document.addEventListener('click', function(event) {{
                if (event.target.classList.contains('popup-overlay')) {{
                    event.target.classList.remove('show');
                    document.body.style.overflow = 'auto';
                }}
            }});
            
            document.querySelectorAll('.popup-content').forEach(el => {{
                el.addEventListener('click', e => e.stopPropagation());
            }});
            
            document.addEventListener('keydown', function(e) {{
                if (e.key === 'Escape') {{
                    document.querySelectorAll('.popup-overlay.show').forEach(popup => {{
                        popup.classList.remove('show');
                        document.body.style.overflow = 'auto';
                    }});
                }}
            }});
        </script>
    </body>
    </html>
    '''
    
    components.html(html_content, height=750, scrolling=False)

# Hyd places
if st.session_state.current_page == "hyderabad":
    st.markdown("<h1 class='main-title'>Happy Valentine's day my Love 💖</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Each heart pinpoint is a core memory that stays in each of our hearts Vasi ❤️‍🔥</div>", unsafe_allow_html=True)
    
    map_base64 = get_base64_image("assets/photos/hyd.png")
    if map_base64:
        create_interactive_map(HYD_LOCATIONS, map_base64, "💖")
        
        # PERFECTLY CENTERED BUTTON
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✈️ Next Destination....shushhhh", key="next_dest", use_container_width=True):
                st.session_state.current_page = "japan"
                st.rerun()
    else:
        st.error("⚠️ Hyderabad map not found!")
        st.info(f"Please add map at: assets/photos/hyd.png")


elif st.session_state.current_page == "japan":
    st.markdown("<h1 class='main-title'>Our Soon to go...Japan Adventure 🗾💖</h1>", unsafe_allow_html=True)

 
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("← Back to Hyderabad", key="back_hyd", use_container_width=True):
            st.session_state.current_page = "hyderabad"
            st.rerun()
    
    japan_map_base64 = get_base64_image("assets/photos/japan.jpg")
    
    if japan_map_base64:
        st.markdown(
            f"""
            <div style="text-align:center; margin-top:20px;">
                <img src="data:image/jpeg;base64,{japan_map_base64}" 
                    style="width:80%; max-width:1200px; border-radius:20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Japan map not found!")
        st.info("Please add Japan map at: assets/photos/japan.jpg")

# Footer
st.markdown("""
<div style="
    background-color: #DFA7AC;
    padding: 5px;
    border-radius: 10px;
    text-align: center;
    color: brown;
    font-size: 1.3em;
    font-family: 'Georgia', serif;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    margin: 40px auto 30px;
    width: 70%;
    max-width: 800px;
">
    I hope to annoy/surprise you for the next 50 Valentine's days 💕
</div>
""", unsafe_allow_html=True)

