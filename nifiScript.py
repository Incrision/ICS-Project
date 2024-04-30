###############################################################################
# Write content to an outgoing flow file using a callback
# modified from "https://community.hortonworks.com/articles/75545/executescript-cookbook-part-2.html"
# 
# This script will read and overwirte content. In this example,
# the input content will not be used for output.
# 
# output:
# !dlroW olleH
###############################################################################



from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import time 
    
# Define a subclass of StreamCallback for use in session.write()
class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass
    def process(self, inputStream, outputStream):
		ts = time.time()
		text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
		text1, text2 = text.split('\n', 1)
		
		text1 = "time, " + text1 + "\n"
		text2 = str(ts) + ", " + text2
		
		text = text1 + text2
		outputStream.write(bytearray(text.encode('utf-8')))
# end class
flowFile = session.get()
if(flowFile != None):
    flowFile = session.write(flowFile, PyStreamCallback())
    
session.transfer(flowFile, REL_SUCCESS)
