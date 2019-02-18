import sys

# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
# number: text = "X-DSPAM-Confidence:    0.8475";

text = "X-DSPAM-Confidence:    0.8475"
delimiterIndex = text.find(":")
numberBeforeParsing = text[delimiterIndex + 1: len(text)]
numberAfterParsing = float(numberBeforeParsing.strip())
print(numberAfterParsing)
