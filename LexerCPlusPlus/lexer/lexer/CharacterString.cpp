/*Valter Nunez A01206138  */
namespace lexer;

#include <string>



class CharacterString : Token {
  //Private stuff
  private:
    string value;
  //Public stuff
  public:
    //Setter
    CharacterString(String value){
      this->tag = Tag.CHARACTERSTRING  //que vergas hace esta linea?
      this->value = value;
    }
    //Getter
    String getValue(){
      return value;
  }
}





/*

package lexer;

public class CharacterString extends Token {
	private String value;

	public CharacterString(String value) {
		super(Tag.CHARACTERSTRING);
		this.value = value;
	}

	public String getValue() {
		return value;
	}
}


 */
