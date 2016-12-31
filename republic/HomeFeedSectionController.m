//
//  HomeFeedSectionController.m
//  republic
//
//  Created by Prabhat Godse on 12/30/16.
//  Copyright © 2016 Prabhat Godse. All rights reserved.
//

#import "HomeFeedSectionController.h"

#import "SenatorFeedCellCollectionViewCell.h"

@interface HomeFeedSectionController()
@property (nonatomic, strong) NSString *object;
@end

@implementation HomeFeedSectionController

- (NSInteger)numberOfItems {
    return 1;
}

- (CGSize)sizeForItemAtIndex:(NSInteger)index {
    return CGSizeMake(self.collectionContext.containerSize.width, 56);
}

- (UICollectionViewCell*)cellForItemAtIndex:(NSInteger)index {
    SenatorFeedCellCollectionViewCell *cell = [self.collectionContext
                                               dequeueReusableCellOfClass:[SenatorFeedCellCollectionViewCell class]
                                               forSectionController:self
                                               atIndex:index];
    cell.fullName = self.object;
    
    return cell;
}

- (void)didUpdateToObject:(id)object {
    self.object = object;
}

- (void)didSelectItemAtIndex:(NSInteger)index {
    
}
@end
