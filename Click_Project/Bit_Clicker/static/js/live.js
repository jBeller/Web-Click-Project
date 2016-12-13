/*
  JSON object format of scores:
  {"scores": [ {"id", "user_name", "score"} ] }
*/

var Score = React.createClass({
  render: function() {
    return(
      <div className="Score">
        <ul>
          <li>{this.props.user} - {this.props.score} bits</li>
        </ul>
      </div>
    );
  }
});

var ScoreList = React.createClass({

  render: function() {
    var ScoreNodes = this.props.data.map(function(s) {
      return (
        <Score user={s.user_name} score={s.score} key={s.id}>
        </Score>
      );
    });

    return(
      <div className="scoreList">
      <h3>Leader Board</h3>
        {ScoreNodes}
      </div>
    );
  }
});

var LeaderBoard = React.createClass({
  loadScores: function() {
    $.ajax({
      url: this.props.url,
      type: "GET",
      cache: false,
      dataType: "json",
      success: function(data) {
        this.setState({data: data.scores});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadScores();
    setInterval(this.loadScores, this.props.pollInterval);
  },
  render: function() {
    return(
      <div className="leaderBoard">
        <ScoreList data={this.state.data} />
      </div>
    );
  },
});
/* Update leaderboard every 30 seconds */
ReactDOM.render(<LeaderBoard url="/scores" pollInterval={30000}/>, document.getElementById('LeaderBoard'));
