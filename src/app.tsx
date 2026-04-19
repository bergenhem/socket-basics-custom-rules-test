// Deliberate vulnerabilities to test SAST rules — DELETE THIS FILE after testing

// org.no-eval
const userInput = "1 + 1"
const result = eval(userInput)

// org.no-function-constructor
const dynamicFn = new Function("a", "b", "return a + b")

// org.no-innerhtml
const el = document.getElementById("app")!
el.innerHTML = "<div>" + userInput + "</div>"

// org.no-dangerously-set-innerhtml (React/JSX)
export default function Vulnerable() {
  return <div dangerouslySetInnerHTML={{ __html: userInput }} />
}