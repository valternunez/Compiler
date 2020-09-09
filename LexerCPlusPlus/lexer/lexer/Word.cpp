//Valter Nunez A01206138
namespace lexer;

#include <string>

class Word : Token {
  private:
    string lexeme;

  public:
    Word(string lexeme, int tag) {
      this->tag = tag;
      this->lexeme = lexeme;
    }
    string getLexeme(){
      return lexeme;
    }
    static const Word eq = new Word( "==", Tag.EQ  ),
      ne = new Word( "<>", Tag.NEQ ),
  		le  = new Word( "<=", Tag.LE  ),
      ge = new Word( ">=", Tag.GE ),
  		minus  = new Word( "minus", Tag.MINUS ),
  		assing = new Word( ":=", Tag.ASSIGN ),
  		True   = new Word( "true",  Tag.TRUE  ),
  		False  = new Word( "false", Tag.FALSE );

}

/*

package lexer;

public class Word extends Token {
	private String lexeme;

	public Word(String lexeme, int tag) {
		super(tag);
		this.lexeme = lexeme;
	}

	public String getLexeme() {
		return lexeme;
	}

	public static final Word
		eq  = new Word( "==", Tag.EQ  ),  ne = new Word( "<>", Tag.NEQ ),
		le  = new Word( "<=", Tag.LE  ),  ge = new Word( ">=", Tag.GE ),
		minus  = new Word( "minus", Tag.MINUS ),
		assing = new Word( ":=", Tag.ASSIGN ),
		True   = new Word( "true",  Tag.TRUE  ),
		False  = new Word( "false", Tag.FALSE );
}


*/
