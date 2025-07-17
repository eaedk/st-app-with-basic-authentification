import streamlit as st

# Streamlit app for Contact Page
def main():
    st.set_page_config(page_title="Contact Page", page_icon="✉️", layout="centered")

    # Title of the page
    st.title("Contact Me")

    # Display LinkedIn Profile Picture and Information
    st.subheader("About Me")
    # Display LinkedIn Profile Picture
    linkedin_picture_url = "https://media.licdn.com/dms/image/v2/C5103AQEWceAkHjUwVw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1582378324719?e=1758153600&v=beta&t=Ycy1ePoKN5-gScHjZybK_lJfzbhASOiwTS_sWpjGapM"
    # st.image(linkedin_picture_url, width=250, caption="Esaïe Alain Emmanuel Dina Koupoh")
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{linkedin_picture_url}" width="250" style="border-radius: 10px;"/>
        </div>
    """, unsafe_allow_html=True)

    st.write("""
             
             
    I'm Esaïe Alain Emmanuel Dina Koupoh, a professional with expertise in various domains including Computer Science and Artificial Intelligence.
    You can view my full profile on [LinkedIn](https://www.linkedin.com/in/esa%C3%AFe-alain-emmanuel-dina-koupoh-7b974a17a/).
    """)
    
    

    # Contact Form Section
    st.subheader("Get in Touch")

    # Form HTML (FormSubmit service)
    contact_form = """
    <form action="https://formsubmit.co/bfa835ba2ae810c75d0c708811592aa8" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send Message</button>
    </form>
    """

    # Display the contact form with a neat design
    st.markdown(contact_form, unsafe_allow_html=True)

    # Improve Page Design with More Styling
    st.markdown("""
    <style>
        .css-1i53xv9 { 
            margin-top: 20px; 
            padding: 10px; 
            font-size: 16px;
        }
        button {
            background-color: #008CBA;
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #005f73;
        }
        textarea {
            width: 100%;
            height: 150px;
            margin-bottom: 20px;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        input[type="text"], input[type="email"] {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
    </style>
    """, unsafe_allow_html=True)

    # Footer Section with Links
    st.subheader("Connect with Me")
    st.markdown("""
    - [LinkedIn](https://www.linkedin.com/in/esa%C3%AFe-alain-emmanuel-dina-koupoh-7b974a17a/)
    - [Huggingface](https://www.huggingface.co/eaedk)
    - [GitHub](https://www.github.com/eaedk)
    - [Email Me](mailto:emmanuelkoupoh@gmail.com)
    """)

if __name__ == "__main__":
    main()
