def selecPath():
    return askdirectory()


def selectFile():
    return askopenfilename(
        title="Open WSD file", filetypes=[("wsd files", ".wsd"), ("all files", ".*")]
    )
