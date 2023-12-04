# style.py
def load_styles():
    return """
    <style>
        :root {
            --primary-color: #FAE4E7;
            --secondary-color: #B7E1FA;
            --accent-color: #A2D1AA;
            --white-color: #FFFFFF;
            --black-color: #000000;
        }

        body {
            font-family: 'Arial', sans-serif;
            color: var(--black-color);
            background-color: var(--white-color);
        }

        h1 {
            color: var(--primary-color);
        }

        .stFileUploader, .stSelectbox, .stMultiselect, .stSlider {
            border: 2px solid var(--secondary-color);
            border-radius: 5px;
        }

        .stButton>button {
            background-color: var(--accent-color);
            color: var(--white-color);
            border-radius: 5px;
            padding: 10px 15px;
        }

        .stButton>button:hover {
            background-color: var(--secondary-color);
        }

        .stImage {
            border-radius: 10px;
        }
    </style>
    """
