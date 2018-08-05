import React, { Component } from "react";
import logo from "../images/sa-logo-small.png";

class Footer extends Component {
  render() {
    return (
      <div className="Footer">
        <div className="footer-column">
          <img src={logo} alt="logo" />
        </div>
        <div className="footer-column">
          <h3>Distance Edit App</h3>
          <div>
            <p>
              Made with ❤️by <strong>Matthew Thorry</strong>, 2018 with
              JavaScript, React, Express and custom CSS
            </p>
            <a
              href="https://github.com/mthorry/jubilant-pancake"
              className="item"
              target="_blank"
            >
              GitHub Repo
            </a>
            <br />
          </div>
        </div>
        <div className="footer-column">
          <h3>Want More?</h3>
          <p>
            Checkout some of my professional accomplisments on{" "}
            <a href="https://www.linkedin.com/in/mthorry" target="_blank">
              LinkedIn
            </a>{" "}
            or 💌 Shoot me an{" "}
            <a
              href="mailto:mthorry@gmail.com?Subject=Nice%20app!"
              target="_top"
            >
              email
            </a>
          </p>
        </div>
      </div>
    );
  }
}

export default Footer;
