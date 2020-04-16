import React, { Component } from 'react';

import { connect } from 'react-redux';

import {
  setCurrentValue,
  closeGalleryView,
} from '../../actions/galleryAction';


export class GalleryLanding extends Component {

  _onHeaderClick = (event) => {
    event.preventDefault();
    if (event.currentTarget === event.target) {
      this.props.closeGalleryView();
    }

  }

  render() {
    if (!this.props.show) {
      return null;
    }

    const { current, images } = this.props;

    let imageUrl = "http://localhost:8000/" + images[current];
    let mainImage = <img src={imageUrl} className="gallery-image" alt="" />
    let smallContent = images.map((image, index) => {
      let imageURL = "http://localhost:8000/" + image;
      return (
        <img className="gallery-image-small" key={index} src={imageURL} alt={image} onClick={() => {
          this.props.setCurrentValue(index);
        }} />
      )
    })

    // let content = "Content";

    return (
      <div className="gallery-container" onClick={this._onHeaderClick}>
        <div className='container'>
          <div className='gallery-main-image'>
            <div className="cross" onClick={() => {
              this.props.closeGalleryView()
            }}>close</div>
            {mainImage}
          </div>
          <div className='gallery-small-images'>
            {smallContent}
          </div>
        </div>
      </div >
    );
  }
}

const mapStateToProps = state => ({
  current: state.gallery.current,
  images: state.gallery.images,
  show: state.gallery.show
});

export default connect(
  mapStateToProps,
  { setCurrentValue, closeGalleryView }
)(GalleryLanding);
