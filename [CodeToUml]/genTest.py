def test(name,throws="",expect=""):
	return "\t@test\n\tpublic void {}(){}".format(name,throws)
TestData ={
	"pack":"competiton",
	"Name":"competitor",
	"test" :
	[test("CreationTest",),test("getterTest")],


}



if __name__ == "__main__":
	print("""
package""",TestData['pack'],""";

import static org.junit.Assert.*;
import org.junit.*;


public class""", TestData['Name']+"""Test{
	
""",'\n'.join(TestData['test']) ,"""




	public static junit.framework.Test suite() {

		return new junit.framework.JUnir4TestAdapter(""", TestData['pack'],TestData['Name'] ,""".class);
	}
}


		""")