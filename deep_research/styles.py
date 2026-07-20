EXAMPLES = [

    "Latest advancements in Generative AI Agents",

    "Future impact of Artificial Intelligence in healthcare",

    "Top open-source Large Language Models in 2026",

    "Commercial applications of Agentic AI"

]



HEADER_HTML = """

<div class="prisma-header">


    <div class="prisma-logo">

        <div class="logo-line line-one"></div>
        <div class="logo-line line-two"></div>
        <div class="logo-line line-three"></div>

    </div>



    <div class="prisma-title">

        <h1>
            PRISMA<span>/</span>AI
        </h1>


        <p>
            Prajwal K.C.'s DeepSearch Intelligence Platform
        </p>

    </div>


</div>

"""

CSS = """

.gradio-container {

    max-width:1100px !important;

    margin:auto !important;

    background:#080b14 !important;

    color:white !important;

    font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif !important;

}



/* HEADER */

.prisma-header {


    display:flex;

    align-items:center;

    gap:25px;

    padding:35px 0;

    border-bottom:
    1px solid rgba(255,255,255,0.15);

    margin-bottom:40px;

}



.prisma-logo {

    display:flex;

    flex-direction:column;

    gap:6px;

}



.logo-line {

    height:8px;

    border-radius:20px;

}



.line-one {

    width:55px;

    background:#00d4ff;

}


.line-two {

    width:40px;

    background:#8b5cf6;

}


.line-three {

    width:25px;

    background:#22c55e;

}



.prisma-title h1 {


    font-size:48px;

    margin:0;

    font-weight:900;

    letter-spacing:-2px;

}



.prisma-title h1 span {

    color:#00d4ff;

}



.prisma-title p {


    margin-top:8px;

    color:#9ca3af;

    font-size:14px;

    letter-spacing:2px;

    text-transform:uppercase;

}




/* INPUT */


#prisma-query textarea {


    background:#111827 !important;

    color:white !important;

    border:

    2px solid #374151 !important;


    border-radius:14px !important;

    padding:18px !important;

    font-size:17px !important;

}



#prisma-query textarea:focus {


    border-color:#00d4ff !important;


    box-shadow:
    0 0 20px rgba(0,212,255,.3)
    !important;

}




/* BUTTON */


#prisma-run {


    background:
    linear-gradient(
        135deg,
        #00d4ff,
        #8b5cf6
    )
    !important;


    border:none !important;

    color:white !important;

    border-radius:14px !important;

    font-weight:800 !important;

    height:60px !important;

}



#prisma-run:hover {


    transform:translateY(-2px);

}




/* EXAMPLES */


.example-title {


    margin-top:35px;

    margin-bottom:15px;

    color:#94a3b8;

    font-size:12px;

    letter-spacing:3px;

}



#prisma-examples button {


    background:#111827 !important;

    color:white !important;

    border:

    1px solid #374151 !important;


    border-radius:12px !important;

}



#prisma-examples button:hover {


    border-color:#00d4ff !important;

}





/* REPORT */


#prisma-report {


    margin-top:40px;

    padding:30px;


    background:#111827;


    border-radius:18px;


    border:

    1px solid #1f2937;


}



#prisma-report h1 {


    color:#00d4ff;

}


#prisma-report h2 {


    color:#8b5cf6;

}



footer {

display:none !important;

}



"""

JS = """

() => {

const box =
document.querySelector(
"#prisma-query textarea"
);


if(box)
{
box.focus();
}


}

"""


