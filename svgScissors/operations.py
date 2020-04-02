import os
import asyncio 

from svgScissors import client

async def createArtFileOfPiece(game, gameCompose, componentCompose, componentGamedata, pieceGamedata, artMetaData, outputDirectory):
    if game == None:
        print("game cannot be None.")
        return
    
    if componentCompose == None:
        print("componentCompose cannot be None.")
        return

    if artMetaData == None:
        print("artMetaData cannot be None.")
        return

    if componentGamedata == None:
        print("componentGamedata cannot be None.")
        return

    if pieceGamedata == None:
        print("pieceGamedata cannot be None.")
        return

    if outputDirectory == None: 
        print("outputDirectory cannot be None.")
        return

    templateFilesDirectory = gameCompose["artTemplatesDirectory"]
    artFilename = "%s.svg" % (artMetaData["templateFilename"])
    artFile = Element(os.path.join(templateFilesDirectory, artFilename)) 

    await addOverlays(artFile, artMetaData["overlays"], game, gameCompose, componentGamedata, pieceGamedata)

    artFileOutputName = ("%s-%s" % (componentCompose["name"], pieceGamedata["name"]))
    artFileOutputFilepath = await createArtfile(artFile, artFileOutputName, outputDirectory)
    
    await textReplaceInFile(artFileOutputFilepath, artMetaData["textReplacements"], game, componentGamedata, pieceGamedata)
    await updateStylesInFile(artFileOutputFilepath, artMetaData["styleUpdates"], game, componentGamedata, pieceGamedata)
    await exportSvgToJpg(artFileOutputFilepath, artFileOutputName, outputDirectory)
    print("Produced %s." % (pieceGamedata["name"]))