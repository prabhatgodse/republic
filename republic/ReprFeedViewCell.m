//
//  ReprFeedViewCell.m
//  republic
//
//  Created by Prabhat Godse on 1/4/17.
//  Copyright © 2017 Prabhat Godse. All rights reserved.
//

#import "ReprFeedViewCell.h"

@interface ReprFeedViewCell()
@property (nonatomic, strong) UIImageView *twitterIcon;
@property (nonatomic, strong) UILabel *twitterLabel;
@end

@implementation ReprFeedViewCell

- (id)initWithFrame:(CGRect)frame {
    self = [super initWithFrame:frame];
    
    self.twitterIcon = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"twitter_icon"]];
    self.twitterIcon.frame = CGRectMake(0, 0, 30, 30);
    [self addSubview:self.twitterIcon];
    
    self.twitterLabel = [[UILabel alloc] initWithFrame:CGRectMake(40, 0, 150, 30)];
    
    self.twitterLabel.textColor = [UIColor blackColor];
    [self addSubview:self.twitterLabel];
    
    self.backgroundColor = [UIColor whiteColor];
    return self;
}

- (void)layoutSubviews {
    [super layoutSubviews];
    
    self.twitterLabel.text = self.twitterid;
}

@end
