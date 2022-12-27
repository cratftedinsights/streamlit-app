import streamlit as st
import requests
from streamlit_lottie import st_lottie 
from PIL import Image 
import numpy as np 

st.set_page_config(page_title="Tasty Dishes and Recipes",page_icon=":spaghetti:",layout="wide")

# to get emojis https://webfx.com/tools/emoji-cheat-sheet/ for webpage emojis

# lottie files for lottie files gifs 

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json() 


# use local css
# add a css file to the web page with theme colors 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

#lottie_anime = load_lottie("https://assets4.lottiefiles.com/packages/lf20_9uevdq78.json")
lottie_anime = load_lottie("https://assets1.lottiefiles.com/packages/lf20_6efbhc0k.json")
chapati = Image.open("chapati.jpg")
leanbelly = Image.open("leanbelly.jpg")

# wrap in a containaer
#HEADER
with st.container():
    left_column,right_column = st.columns(2)
    with left_column:
        st.title("CHAPATI")
        st.header("Best chapati cooking method")
        st.write(
           """
        Luckily in our household my Mom has taught us countless times on how to cook chapatis.
        As I stood in the kitchen with my mother, watching her expertly roll out the dough for chapatis, 
        I couldn't help but feel a sense of excitement. You see, my mother had a secret recipe for making
        the perfect chapatis - one that had been passed down through our family for generations 
        to which my grandmother was good and a pro at it.

        The key to the recipe was in the dough, which my mother mixed by hand using a combination of whole
        wheat flour, water, and a secret blend of carrots and boiled pumkin. As she mixed the ingredients together, she explained 
        to me the importance of getting the right consistency - not too dry, not too sticky.

        Once the dough was mixed, my mother began to roll it out, using a rolling pin to get it to the perfect 
        thickness. She then used a small, sharp knife to cut the dough into circular shapes, carefully 
        placing each one on a floured surface as she went.

        As the chapatis cooked on the stove, the aroma of the cooking filled the kitchen, 
        tantalizing our senses. My mother expertly flipped each chapati, making sure that it 
        cooked evenly on both sides.

        Finally, it was time to eat. My mother placed the hot chapatis on the table, 
        along with a variety of accompaniments such as beef stew with vegetables and homemade yogurt. 
        As we sat down to enjoy the fruits of our labor, I couldn't help but feel grateful 
        to my mother for sharing this secret recipe with me. I knew that I would cherish 
        this memory - and the delicious chapatis - for years to come.


        """
        )
    with right_column:
        st.image(chapati,caption='Tasty chapati', width=None, use_column_width=None)
       
   
with st.container():
    st.write("---")
    st.header("INGREDIENTS")
    st.write("##")
    st.write(
        """
            3 cups of flour

            1 1/2 cups of warm water 

            1 tsp of salt   

            1 tsp of sugar  

            vegetable oil for frying  

            2 carrots   

            1/4 slice pumkin       
        """
    )
    st.write("---")
    st.header(":point_down: For fitness and health")
    st.write("Get Lean Belly 3x and eliminate belly fat")
    st.write("[Learn More >](https://www.digistore24.com/redir/370257/MKelvin/)")  

with st.container():
    st.write("---")
    st.header("Cooking method")
    st.write("##")
    st.subheader("How to cook")
    st.write("##")
    left_column,right_column = st.columns(2)
    with left_column:
        st.write(
            """
            1. Slice the pumkin into pieces and boil it 
               with medium heat until its soft.Rinse the water carefully leaving only
               the boiled pumkin.

            2. Crash the boiled pumkin (step 1) with a wooden spoon or a strong spoon to
               produce a fine mixture with no lumps.

            3. Wash the carrots well and grate them using a grater for small 
               fine segments.

            3. Place the fine mixture (step 2) and the fine grated carrots (step 3) in a bowl and 
                add 3 cups of flour.
    
            4. Add salt, sugar, 2 tbsp of oil and 1 ½ cups of water in a separate jar/ bowl.
               Stir until the salt and sugar dissolves.

            5. Add the liquid mixture in (step 4) in the bowl (step 3) and mix well.

            """
        )
     # animations are added by lottie files 
    
    with right_column:
        st_lottie(lottie_anime,height=300,key="stir")
        st.write("stir and mix well")

    st.write(
        """
        6. Keep kneading for 10 minutes and add flour if needed until the dough becomes non-sticky. 
           Add 2-3 tbsp of oil and continue kneading until the oil mixes well and the dough
           is soft. Cover the dough and leave it for 40 minutes.

        7. After the 40 minutes, divide the dough into 10 - 15 equal parts making ball like shapes. 
           Arrange them in a flat surface dusted with flour(Cover with a damp tablecloth to avoid drying).

        8. Dust flour in the flat place and take one of the balls and start rolling with a 
           rolling pin to a circular shape, brush oil on top and roll it inwards to form a shape-like a rope, 
           then create a coil-like shape and press the ball down with your palm to make it flat. 
           Repeat this process to the rest of the remaining balls of dough.

        9. Next, start rolling each of the coil-like shape doughs with the 
           rolling pin to form a circular shape again.

        10. In a hot pan, place the rolled out circular chapati and
            fry each side with little oil until its golden brown on medium heat.
            Place your cooked chapati in a flat plat and cover with an aluminum foil.

        11. Repeat this step to the rest of the coil-like dough.

        **Serve with your favourite stew and also feel free to eat them for breakfast with either, tea
        drinking chocolate or pure milk so so tasty and sweet.
        
          """
        )
with st.container():
    st.write("--=")
    st.header("Get Lean Belly 3x ")
    st.write("##")
    text_column,image_column = st.columns((1,2))
    with image_column:
        st.image(leanbelly)
    with text_column:
        st.subheader("How to eliminate belly fat with a proven method fast and easy")
        st.markdown("[Learn More >](https://www.digistore24.com/redir/370257/MKelvin/)")
        st.write(
            """
            Q: What specifically makes LeanBelly 3X the best supplement of its kind?

            While there are 28 different CLA types (or, isomers), in nature, the most important isomer is cis-9, trans-11 (c9,t11). When it comes to a toning supplement, however, there are two isomers critical for maximum effectiveness and benefits. Both the c9,t11 isomer mentioned and the trans-10, cis-12 (t10,c12) isomer, and both need to be provided in equal amounts to experience the synergistic effects that contribute to provide CLA benefits.†
           """
           )
        st.markdown("[Learn More >](https://www.digistore24.com/redir/370257/MKelvin/)")
    st.write(
           """
            Speaking of the benefits of this body-toning supplement, experimental research has shown conjugated linoleic acid may work with the body's enzymes involved in fat mobilization and storage to help support healthy body composition.† More than a dozen human studies have shown that supplementation with CLA may help reduce body fat while maintaining (and in some cases, increasing) calorie-burning muscle, ultimately helping support quality weight and that lean, toned look we've talked about.†

            As a testament to conjugated linoleic acid being a true body toner, four separate systematic reviews with meta-analysis (which many would argue represent the gold standard for scrutinizing and summarizing scientific research on a given topic) have concluded that supplementing with conjugated linoleic acid may help reduce body fat and maintain (or increase) lean muscle.†

            Q: What is the best way to use LeanBelly 3X?

            Simply take 2 gel caps with your first and last meal of the day and let science do the rest. And if you forget to take it, feel free to take a double serving (4 gel caps) with lunch or dinner.

            Q: How long will a bottle of LeanBelly 3X last?

            Each bottle contains 30 servings. The daily recommended dosage provides the exact amount proven in scientific research to be the most beneficial.

            Q: Does this product contain caffeine or any other stimulants?

            No. This product is caffeine and stimulant-free.

            Q: Are there any allergy concerns with this product?
            This product is manufactured in a facility that also processes tree nuts, peanuts, wheat, and soy. Always review the label for the most accurate information.

            Q: If I have a medical condition, can I take this product?

            LeanBelly 3X is intended for use by healthy adults over 18 years old. Do not take this product if you are pregnant or nursing. Consult your physician before use if you are taking any prescription or over-the-counter medications or are being treated for any medical condition. Discontinue use and consult your physician if you experience any adverse reaction to this product.

            Q: Is it safe to order online from your web site?

            Yes. We use a 256-bit secure ordering server so you are protected the same as if you were ordering from Amazon.com or any other trusted Web site.

            Q: What if this product doesn't work for me?

            While LeanBelly 3X is backed by science and was created to work, if for any reason at all you are unsatisfied with your purchase, just let us know, and we will issue a prompt and courteous refund even on empty bottles. You're always protected by our industry best 60-Day Money Back Guarantee.                      
          """
        )
    st.markdown("[Learn More >](https://www.digistore24.com/redir/370257/MKelvin/)")
# contact form 
with st.container():
    st.write("--=")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/kelvinmainamt@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()