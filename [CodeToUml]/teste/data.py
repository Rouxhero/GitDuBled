 #!/usr/bin/env python3

head = lambda package,className : """
{}

import static org.junit.Assert.*;
import org.junit.*;


public class {}Test
""".format(package,className)


funcR = r'(protected|public|private)\s?([\w][\w]*)?\s([\w][\w]*)(\(([\w]+\s[\w]+,?\s?)*\))'


