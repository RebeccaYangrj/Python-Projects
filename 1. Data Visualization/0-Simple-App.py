import justpy as jp

#after each time run just control + C to quit the current program, then run again

def app():
    wp = jp.QuasarPage()
    # h1 is the headline and the QDiv is quaser webpage
    # a=wp means h1 belong to wp
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes ="text-h3 text-weight-bold text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text = "These graphs represent course review analysis")
    return wp

#call this function, just use the name not the app()
jp.justpy(app)