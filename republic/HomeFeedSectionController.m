//
//  HomeFeedSectionController.m
//  republic
//
//  Created by Prabhat Godse on 12/30/16.
//  Copyright © 2016 Prabhat Godse. All rights reserved.
//

#import "HomeFeedSectionController.h"

#import "ReprFeedViewCell.h"
#import "ReprDataModel.h"

@interface HomeFeedSectionController()
@property (nonatomic, strong) ReprDataModel *object;
@end

@implementation HomeFeedSectionController

- (NSInteger)numberOfItems {
    return 1;
}

- (CGSize)sizeForItemAtIndex:(NSInteger)index {
    return CGSizeMake(self.collectionContext.containerSize.width, 56);
}

- (UICollectionViewCell*)cellForItemAtIndex:(NSInteger)index {
    ReprFeedViewCell *cell = [self.collectionContext
                              dequeueReusableCellOfClass:[ReprFeedViewCell class]
                              forSectionController:self
                              atIndex:index];
    
    cell.twitterid = self.object.twitter;
    
    return cell;
}

- (void)didUpdateToObject:(id)object {
    self.object = object;
}

- (void)didSelectItemAtIndex:(NSInteger)index {
    
}
@end
