import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import WelcomeComponent from './components/WelcomeComponent.jsx';
import DashboardComponent from './components/DashboardComponent.jsx';
import FormComponent from './components/FormComponent.jsx';
import HistoryComponent from './components/HistoryComponent.jsx';
import SavedComponent from './components/SavedComponent.jsx';
import ResultComponent from './components/ResultComponent.jsx';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('WelcomeComponent renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App><WelcomeComponent /></App>, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('DashboardComponent renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App><DashboardComponent/></App>, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('FormComponent renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App><FormComponent /></App>, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('HistoryComponent renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App><HistoryComponent /></App>, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('SavedComponent renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App><SavedComponent /></App>, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('ResultComponent renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App><ResultComponent /></App>, div);
  ReactDOM.unmountComponentAtNode(div);
});
