//
//  SenatorFeedCellCollectionViewCell.m
//  republic
//
//  Created by Prabhat Godse on 12/30/16.
//  Copyright © 2016 Prabhat Godse. All rights reserved.
//

#import "SenatorFeedCellCollectionViewCell.h"

@interface SenatorFeedCellCollectionViewCell ()
@property (nonatomic, strong) UILabel *label;
@end

@implementation SenatorFeedCellCollectionViewCell

- (void)layoutSubviews {
    [super layoutSubviews];
    if(_label == nil) {
        _label = [[UILabel alloc] initWithFrame:self.bounds];
        [self addSubview:_label];
    }
    _label.backgroundColor = [UIColor whiteColor];
    _label.textColor = [UIColor blackColor];
    _label.text = self.fullName;
}

@end
