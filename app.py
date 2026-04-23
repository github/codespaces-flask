from flask import Flask, request, send_file, render_template_string
import pandas as pd
from io import BytesIO

app = Flask(__name__)

# ---------------- SORT ORDER ---------------- #

SHAPE_ORDER = [
    "ROUND","ROU.MOD.","OVAL","OV.MOD.","STEP OVAL",
    "PEAR","PE.MOD.","STEP PEAR",
    "MARQUISE","MQ.MOD","STEP MARQUISE",
    "PRINCESS","RAD","SQ.RAD",
    "EMERALD","ASSCHER","SQ.CUS.","SQ.CUS.MOD.","LO.CUS.",
    "HEXAGON","HEART"
]

SIZE_ORDER = [
    "10.000-10.999","9.000-9.999","8.000-8.999","7.000-7.999",
    "6.000-6.999","5.500-5.999","5.000-5.499","4.500-4.749",
    "4.250-4.499","4.000-4.249","3.750-3.999","3.500-3.749",
    "3.250-3.499","3.000-3.249","2.750-2.999","2.500-2.749",
    "2.250-2.499","2.000-2.249","1.900-1.999","1.800-1.899",
    "1.700-1.799","1.600-1.699","1.500-1.599","1.400-1.499",
    "1.300-1.399","1.200-1.299","1.100-1.199","1.000-1.099",
    "0.960-0.999","0.900-0.959","0.700-0.799","0.500-0.599","0.400-0.459"
]

CLARITY_ORDER = ["FL","IF","VVS1","VVS2","VS1","VS2","SI1","SI2","SI3","PRE","STD"]

DZ_COLOR_ORDER = [
    "D","E","F","G","H","I","J","K","L","M","N","O",
    "P","Q","R","S","T","U","V","W","X","Y","Z","PRE","STD"
]

FANCY_COLOR_ORDER = [
    "YELLOW","BLUE","PINK","FANCY LIGHT YELLOW","FANCY YELLOW",
    "FANCY INTENSE YELLOW","FANCY VIVID YELLOW",
    "FANCY PINK","FANCY INTENSE PINK","FANCY VIVID PINK",
    "FANCY BLUE","FANCY INTENSE BLUE","FANCY VIVID BLUE"
]

# ---------------- HTML ---------------- #

HTML = """
<h2>Universal File Sorter (Diamond MIS)</h2>

<form method="post" enctype="multipart/form-data">
    <input type="file" name="file" required>
    <button type="submit">Sort File</button>
</form>

<p>Upload Excel/CSV → Get Sorted File Download</p>
"""

# ---------------- SORT ENGINE ---------------- #

def apply_sort(df):

    df.columns = [c.strip().lower() for c in df.columns]

    def sort_col(col, order):
        if col in df.columns:
            df[col] = df[col].astype(str).str.upper()
            df[col] = pd.Categorical(df[col], categories=order, ordered=True)

    # Shape
    sort_col("shape", SHAPE_ORDER)

    # Size
    sort_col("size range", SIZE_ORDER)

    # Clarity
    sort_col("clarity", CLARITY_ORDER)

    # Color
    if "color" in df.columns:
        df["color"] = df["color"].astype(str).str.upper()

        if df["color"].str.contains("FANCY").any():
            order = FANCY_COLOR_ORDER
        else:
            order = DZ_COLOR_ORDER

        df["color"] = pd.Categorical(df["color"], categories=order, ordered=True)

    # sort by priority columns
    sort_cols = [c for c in ["shape","size range","color","clarity"] if c in df.columns]
    df = df.sort_values(sort_cols)

    return df


# ---------------- HOME ---------------- #

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML)


# ---------------- PROCESS FILE ---------------- #

@app.route("/", methods=["POST"])
def process():

    file = request.files["file"]

    if file.filename.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    df = apply_sort(df)

    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    return send_file(
        output,
        download_name="sorted_file.xlsx",
        as_attachment=True
    )


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)
