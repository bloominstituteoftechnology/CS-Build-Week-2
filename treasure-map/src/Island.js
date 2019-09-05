import React, { Component } from 'react';
import P5Wrapper from 'react-p5-wrapper';
import './App.css';

class Island extends Component {
  constructor(){
    super();
    this.state = {color:[Math.random()*255, Math.random()*255, Math.random()*255]};
    this.randomColor = this.randomColor.bind(this);
  }

  randomColor(){
    this.setState({color:[Math.random()*255, Math.random()*255, Math.random()*255]}
    )
  }


  sketch(p){
    let canvas;

    function circle() {
        let x = 50;
        while (x<=1000) {
            p.stroke(0);
            p.strokeWeight(10);
            p.line(x, 100, x+100, 100);

            p.stroke(0);
            p.strokeWeight(0);
            p.ellipse(x, 100, 50, 50);
            x+=100
        }
    }

    p.setup = () => {
      canvas = p.createCanvas(1000, 800);
      p.noStroke();
    }

    p.draw = () => {
      p.background('orangered');
      circle()

    }

    p.myCustomRedrawAccordingToNewPropsHandler = (newProps) => {
      if(canvas) //Make sure the canvas has been created
        p.fill(newProps.color);
    }
}

  render() {
    return (
      <div>
        <P5Wrapper sketch={this.sketch} color={this.state.color}></P5Wrapper>
      </div>
    );
  }
}

export default Island;